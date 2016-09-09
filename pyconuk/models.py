from django.db import models
from django_amber.models import ModelWithContent, ModelWithoutContent


class Page(ModelWithContent):
    title = models.CharField(max_length=255)
    callout_big_1 = models.CharField(max_length=255)
    callout_big_2 = models.CharField(max_length=255)
    callout_small = models.CharField(max_length=255)
    tito_required = models.BooleanField(default=False)
    show_sponsors = models.BooleanField(default=True)

    dump_dir_path = 'pages'


class NewsItem(ModelWithContent):
    title = models.CharField(max_length=255)
    date = models.DateField()

    dump_dir_path = 'news'


class Speaker(ModelWithContent):
    name = models.CharField(max_length=255)

    dump_dir_path = 'speakers'


class Session(ModelWithContent):
    speaker = models.ForeignKey(Speaker, null=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)

    dump_dir_path = 'sessions'

    def session_type(self):
        return self.key.split('/', 1)[0]

    def slug(self):
        return self.key.split('/', 1)[1]

    def slot(self):
        return self.scheduleslot_set.order_by('time')[0]

    def time(self):
        return self.slot().time

    def date(self):
        return self.slot().date

    def day(self):
        return self.date().split()[0]

    def room(self):
        return self.slot().room


class Sponsor(ModelWithContent):
    TIERS = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('partner', 'partner'),
    )
    name = models.CharField(max_length=255)
    tier = models.CharField(max_length=255, choices=TIERS)
    website = models.CharField(max_length=255, null=True)
    twitter_handle = models.CharField(max_length=255, null=True)
    logo_filename = models.CharField(max_length=255, null=True)

    dump_dir_path = 'sponsors'


class Redirection(ModelWithoutContent):
    new_url = models.CharField(max_length=255)

    dump_dir_path = 'redirections'

    def original_url(self):
        return '/{}/'.format(self.key)


class ScheduleSlot(ModelWithoutContent):
    session = models.ForeignKey(Session, null=True)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=40)
    room = models.CharField(max_length=40)
    time = models.CharField(max_length=40)

    dump_dir_path = 'schedule'
