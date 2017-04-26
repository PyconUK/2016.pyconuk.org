from django.core.urlresolvers import reverse

from .models import ScheduleSlot


def load_schedule_context(date, rooms_in_order):
    slots = ScheduleSlot.objects.filter(date=date)

    rooms_in_use_on_day = {slot.room for slot in slots}
    rooms = [room for room in rooms_in_order if room in rooms_in_use_on_day]

    times = sorted({slot.time for slot in slots})

    slots_by_room_and_time = {}

    for slot in slots:
        if slot.session:
            session = slot.session
            if session.session_type() == 'keynotes':  # Yes, it'd be nicer if the session_type was singular, but it's not
                text = 'Keynote: {}'.format(session.title)
            else:
                text = session.title
            url = reverse('session', args=[session.session_type(), session.slug()])
            speaker = session.speaker.name
            chair = slot.chair
        else:
            text = slot.title
            url = None
            speaker = None
            chair = None

        slots_by_room_and_time[(slot.room, slot.time)] = {
            'text': text,
            'url': url,
            'speaker': speaker,
            'chair': chair,
            'room': slot.room,
        }

    slots_table = [
        [time] + [slots_by_room_and_time.get((room, time)) for room in rooms]
        for time in times
    ]

    slots_table_with_dimensions = compute_html_table_dimensions(slots_table)

    return {
        'date': date,
        'day': date.split()[0].lower(),
        'rooms': rooms,
        'table': slots_table_with_dimensions
    }


def same_session(session1, session2):
    if not isinstance(session1, dict) or not isinstance(session2, dict):
        return bool(session1 == session2)
    else:
        return bool(
            session1['text'] == session2['text']
            and session1['url'] == session2['url']
            and session1['speaker'] == session2['speaker']
            and session1['chair'] == session2['chair']
        )

def compute_html_table_dimensions(table):
    table_with_dimensions = []

    n_rows = len(table)
    n_cols = len(table[0])

    for row_ix in range(n_rows):
        row = []

        for col_ix in range(n_cols):
            value = table[row_ix][col_ix] 

            if value is None:
                row.append({'value': value, 'width': width, 'height': height})

            else:
                if col_ix == 0 or not same_session(table[row_ix][col_ix],
                                                   table[row_ix][col_ix - 1]):
                    if row_ix == 0 or not same_session(table[row_ix][col_ix],
                                                       table[row_ix - 1][col_ix]):
                        width = 1
                        height = 1

                        while col_ix + width < n_cols:
                            if same_session(table[row_ix][col_ix + width], value):
                                width += 1
                            else:
                                break

                        while row_ix + height < n_rows:
                            if same_session(table[row_ix + height][col_ix], value):
                                height += 1
                            else:
                                break

                        row.append({'value': value, 'width': width, 'height': height})

        if row:
            table_with_dimensions.append(row)

    return table_with_dimensions


def logo_css(width, height):
    """Compute the width and padding values to layout a sponsor logo.
    """
    scaled_width =  int(round(width * 100 / height))
    padding =       int(round(height / width * 100))
    return {'scaled_width': scaled_width, 'padding': padding}


if __name__ == '__main__':
    table = [
        ['A', 'B', 'B', 'B'],
        ['A', 'C', 'C', 'C'],
        ['D', 'C', 'C', 'C'],
    ]

    result = [
        [{'value': 'A', 'width': 1, 'height': 2}, {'value': 'B', 'width': 3, 'height': 1}],
        [{'value': 'C', 'width': 3, 'height': 2}],
        [{'value': 'D', 'width': 1, 'height': 1}],
    ]

    assert compute_html_table_dimensions(table) == result

    table = [
        ['A', 'A'],
        ['A', 'B'],
    ]

    result = [
        [{'value': 'A', 'width': 1, 'height': 2}],
        [{'value': 'A', 'width': 1, 'height': 1}, {'value': 'B', 'width': 1, 'height': 1}],
    ]

    assert compute_html_table_dimensions(table) == result
