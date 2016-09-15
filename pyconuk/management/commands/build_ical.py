import datetime

import pytz
import vobject
import yaml

from django.core.management.base import BaseCommand

from pyconuk.models import Session


TALK_PREFIXES = ('talks/', 'workshops/', 'keynotes/')


def dt_from_d_and_t(date, time):
    return datetime.datetime.strptime(
        " ".join([date, "September 2016", time]), "%A %dth %B %Y %H:%M"
    )


def add_tz(dt):
    return pytz.UTC.localize(dt - datetime.timedelta(hours=1))


now = datetime.datetime.now()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        cal = vobject.iCalendar()
        cal.add('x-wr-calname').value = 'PyCon UK 2016 Schedule'

        with open('schedule.yml') as f:
            schedule = yaml.load(f.read())

        # This loop has a runtime of O(terrifying), but I stole it from Peter
        # so I don't mind.
        for date in schedule:
            for room in schedule[date]:
                # At this point, the sessions are keyed by session chair. We'd
                # rather iterate over them by time, and we don't care about the
                # session chair. So let's build a list, and then sort it by
                # time.
                sessions = []

                for chairs in schedule[date][room]:
                    for chair in chairs:
                        for time in chairs[chair]:
                            session = chairs[chair][time]
                            dt = dt_from_d_and_t(date, time)
                            sessions.append((dt, session))

                sessions = sorted(sessions, key=lambda x: x[0])

                # Now we want to coalesce the sessions. If there are sessions
                # with the same name, they are actually the same session. We
                # want to remove them.
                indexes_to_drop = []
                previous_session = ''
                for index, (_, name) in enumerate(sessions):
                    if name == previous_session:
                        indexes_to_drop.append(index)

                    previous_session = name

                for index in reversed(indexes_to_drop):
                    del sessions[index]

                # Now, we need the end datetimes. We work this out by noting
                # that each session runs until the next. Some sessions are
                # empty, which means we can ignore them: one session each day
                # is called 'Close', which we can also ignore.
                print("Writing sessions for {} {}".format(date, room))
                for i, (start_time, session_name) in enumerate(sessions):
                    # Empty session, no entry.
                    if not session_name:
                        print("\tNo session at {}".format(start_time))
                        continue

                    # End of the day
                    if session_name == "Close":
                        print("\tEnd of day at {}".format(start_time))
                        break

                    # We have an event! The "end" date of this event is simply
                    # the start date of the next one.
                    event = cal.add('vevent')
                    end_time = sessions[i + 1][0]

                    if session_name.startswith(TALK_PREFIXES):
                        s = Session.objects.get(key=session_name)
                        abstract = s.content
                        speaker_name = s.speaker.name
                        title = s.title
                        room = s.room()

                        event.add("summary").value = "{} - {}".format(
                            title, speaker_name
                        )
                        event.add("description").value = abstract
                        print("\tName: {} - {}".format(title, speaker_name))
                    else:
                        # This is a break, or something similar: we don't need
                        # to look it up in any way.
                        event.add("summary").value = session_name
                        print("\tName: {}".format(session_name))

                    event.add("location").value = room
                    event.add("dtstart").value = add_tz(start_time)
                    event.add("dtend").value = add_tz(end_time)
                    event.add("dtstamp").value = now
                    print("\t\tStart: {}, End {}".format(start_time, end_time))

        with open('schedule.ics', 'w') as f:
            f.write(cal.serialize())
