import os

from django.conf import settings

import django_tables2 as tables


class StatTable(tables.Table):
    post_title = tables.Column()
    today = tables.Column()
    one_day_ago = tables.Column(verbose_name='1 day ago')
    two_days_ago = tables.Column(verbose_name='2 days ago')
    three_days_ago = tables.Column(verbose_name='3 days ago')
    four_days_ago = tables.Column(verbose_name='4 days ago')
    five_days_ago = tables.Column(verbose_name='5 days ago')
    six_days_ago = tables.Column(verbose_name='6 days ago')
    total = tables.Column()

    class Meta:
        attrs = {'class': 'paleblue'}
        template = os.path.join(settings.BASE_DIR, 'stats/templates/stats/site_stat_table.html')
