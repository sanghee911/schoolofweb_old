from django.views.generic.base import TemplateView
from django.utils import timezone
from .tables import StatTable
from blog.models import Post


class StatView(TemplateView):
    template_name = 'stats/stats.html'

    def get_context_data(self, **kwargs):
        context = super(StatView, self).get_context_data(**kwargs)
        date_dict = self.get_days(7)
        now = timezone.now()
        all_posts = Post.objects.all().filter(published='published').filter(published_time__lte=now)
        dict_keys = ['post_title', 'today', 'one_day_ago', 'two_days_ago', 'three_days_ago',
                     'four_days_ago', 'five_days_ago', 'six_days_ago', 'total']

        table_rows = []

        for post in all_posts:
            data_row = [post.title]

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
        context['table'] = table

        return context

    @staticmethod
    def get_days(days):
        seven_days = []
        today = timezone.now()
        for i in range(days):
            date_obj = today - timezone.timedelta(days=i)
            seven_days.append({'year': date_obj.year, 'month': date_obj.month, 'day': date_obj.day})

        return seven_days

    @staticmethod
    def get_hitcount_for_days(obj, **day_dict):
        return obj.hitcount_by_date(**day_dict)


