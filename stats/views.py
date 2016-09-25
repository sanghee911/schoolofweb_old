# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.utils import timezone
from django_tables2 import RequestConfig
from hitcount.models import Hit
from blog.models import Post
from .tables import StatTable


class StatView(TemplateView):
    template_name = 'stats/stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatView, self).get_context_data(**kwargs)
        date_dict = self.get_days(7)
        now = timezone.now()
        all_posts = Post.objects.all().filter(published='published').filter(published_time__lte=now)
        dict_keys = ['post', 'today', 'one_day_ago', 'two_days_ago', 'three_days_ago',
                     'four_days_ago', 'five_days_ago', 'six_days_ago', 'total']

        table_rows = []

        for post in all_posts:
            data_row = [post]

            # get week data for one post
            for date in date_dict:
                count = post.hitcount_by_date(**date)
                data_row.append(count)

            data_row.append(post.hitcount())

            week_data = {}

            # make dict
            for key, value in zip(dict_keys, data_row):
                week_data[key] = value

            table_rows.append(week_data)

        table = StatTable(table_rows)
        RequestConfig(self.request).configure(table)

        context['table'] = table
        # footer data
        context['total_hits'] = self.get_week_hitcounts()

        # meta content
        context['meta_title'] = 'schoolofweb.net Page Analytics'
        context['meta_description'] = '웹 개발, 파이썬, 장고, 리눅스 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.'
        context['meta_keywords'] = '무료 인터넷 강좌, 파이썬, 장고, 리눅스, Python, Django, Linux'
        context['meta_author'] = '이상희, Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context

    @staticmethod
    def get_days(days):
        seven_days = []
        today = timezone.localtime(timezone.now())
        for i in range(days):
            date_obj = today - timezone.timedelta(days=i)
            seven_days.append({'year': date_obj.year, 'month': date_obj.month, 'day': date_obj.day})

        return seven_days

    @staticmethod
    def get_hitcount_for_days(obj, **day_dict):
        return obj.hitcount_by_date(**day_dict)

    def get_week_hitcounts(self):
        date_dict = self.get_days(7)
        dict_keys = ['today', 'one_day_ago', 'two_days_ago', 'three_days_ago',
                     'four_days_ago', 'five_days_ago', 'six_days_ago']
        all_hits = {}
        all_hit_objs = Hit.objects.all()
        for key, date in zip(dict_keys, date_dict):
            all_hits[key] = all_hit_objs.filter(
                created__year=date['year'],
                created__month=date['month'],
                created__day=date['day']
            ).count()

        all_hits['total'] = all_hit_objs.count()

        return all_hits



