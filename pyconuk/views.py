from django.shortcuts import get_object_or_404, render

from .models import Page, NewsItem, Redirection, Session, Speaker, Sponsor
from .utils import load_schedule_context


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

    dates = ['Thursday 15th', 'Friday 16th', 'Saturday 17th', 'Sunday 18th']
    rooms_in_order = ['Cardiff University', 'Assembly Room', 'Room D', 'Ferrier Hall', 'Room C']
    schedules = [load_schedule_context(date, rooms_in_order) for date in dates]

    context = {
        'schedules': schedules,
    }

    return render(request, template, context)


def open_day_view(request):
    template = 'open_day.html'

    date = 'Thursday 15th'
    rooms_in_order = ['Open Day at Cardiff University']

    context = {
        'schedule': load_schedule_context(date, rooms_in_order),
        'tito_required': True,
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
