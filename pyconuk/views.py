from django.shortcuts import get_object_or_404, render

from .models import Page, NewsItem, Redirection, Session, Speaker, Sponsor, ScheduleSlot
from .utils import compute_html_table_dimensions


def page_view(request, key='index'):
    try:
        page = Page.objects.get(key=key)
    except Page.DoesNotExist:
        redirection = get_object_or_404(Redirection, key=key)
        template = 'redirection.html'
        context = {'url': redirection.new_url}
        return render(request, template, context)

    assert page.content_format in ['html', 'md'], 'Page content must use HTML or Markdown'

    template = 'page.html'

    context = {
        'content': page.content,
        'content_format': page.content_format,
        'title': page.title,
        'callout_big_1': page.callout_big_1,
        'callout_big_2': page.callout_big_2,
        'callout_small': page.callout_small,
        'tito_required': page.tito_required,
    }

    return render(request, template, context)


def schedule_view(request):
    template = 'schedule.html'

    dates = ['Friday 16th', 'Saturday 17th', 'Sunday 18th']

    schedules = []

    for date in dates:
        slots = ScheduleSlot.objects.filter(date=date)

        all_rooms = ['Assembly Room', 'Room D', 'Ferrier Hall', 'Room C']
        rooms_in_use_on_day = {slot.room for slot in slots}
        rooms = [room for room in all_rooms if room in rooms_in_use_on_day]

        times = sorted({slot.time for slot in slots})

        slots_by_room_and_time = {
            (slot.room, slot.time): slot.session.title if slot.session else slot.title
            for slot in slots
        }

        slots_table = [
            [time] + [slots_by_room_and_time.get((room, time)) for room in rooms]         
            for time in times
        ]

        slots_table_with_dimensions = compute_html_table_dimensions(slots_table)

        schedules.append({
            'date': date,
            'day': date.split()[0].lower(),
            'rooms': rooms,
            'table': slots_table_with_dimensions
        })

    context = {
        'schedules': schedules,
    }

    return render(request, template, context)


def news_items_view(request):
    news_items = NewsItem.objects.order_by('-date')

    template = 'news_items.html'

    context = {
        'news_items': news_items,
    }

    return render(request, template, context)


def news_item_view(request, datestamp, key):
    news_item = get_object_or_404(NewsItem, key=key)

    assert news_item.content_format in ['html', 'md'], 'NewsItem content must use HTML or Markdown'

    template = 'news_item.html'

    context = {
        'content': news_item.content,
        'content_format': news_item.content_format,
        'title': news_item.title,
        'date': news_item.date,
    }

    return render(request, template, context)


def session_view(request, session_type, slug):
    key = '{}/{}'.format(session_type, slug)
    session = get_object_or_404(Session, key=key)
    speaker = session.speaker

    assert session.content_format in ['html', 'md'], 'Session content must use HTML or Markdown'

    template = 'session.html'

    context = {
        'content': session.content,
        'content_format': session.content_format,
        'title': session.title,
        'speaker': speaker,
    }

    return render(request, template, context)


def speaker_view(request, key):
    speaker = get_object_or_404(Speaker, key=key)
    sessions = speaker.session_set.all()

    assert speaker.content_format in ['html', 'md'], 'Speaker content must use HTML or Markdown'

    template = 'speaker.html'

    context = {
        'content': speaker.content,
        'content_format': speaker.content_format,
        'name': speaker.name,
        'sessions': sessions,
    }

    return render(request, template, context)


def sponsor_view(request, key):
    sponsor = get_object_or_404(Sponsor, key=key)

    assert sponsor.content_format in ['html', 'md'], 'Speaker content must use HTML or Markdown'

    template = 'sponsor.html'

    context = {
        'content': sponsor.content,
        'content_format': sponsor.content_format,
        'name': sponsor.name,
        'tier': sponsor.tier,
        'website': sponsor.website,
        'twitter_handle': sponsor.twitter_handle,
        'logo_filename': sponsor.logo_filename,
    }

    return render(request, template, context)
