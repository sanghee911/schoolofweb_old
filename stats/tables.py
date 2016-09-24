# -*- coding: utf-8 -*-
import os

from django.conf import settings

import django_tables2 as tables


class StatTable(tables.Table):
    post = tables.TemplateColumn(template_name='stats/post_link.html', verbose_name='포스트 제목')
    today = tables.Column(verbose_name='오늘')
    one_day_ago = tables.Column(verbose_name='1일전')
    two_days_ago = tables.Column(verbose_name='2일전')
    three_days_ago = tables.Column(verbose_name='3일전')
    four_days_ago = tables.Column(verbose_name='4일전')
    five_days_ago = tables.Column(verbose_name='5일전')
    six_days_ago = tables.Column(verbose_name='6일전')
    total = tables.Column(verbose_name='통산 합계')

    class Meta:
        attrs = {'class': 'paleblue'}
        template = os.path.join(settings.BASE_DIR, 'stats/templates/stats/site_stat_table.html')
