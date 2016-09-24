from blog.models import Post
from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from django.utils import timezone


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        now = timezone.now()
        return Post.objects.filter(published='published').filter(published_time__lte=now)

    def lastmod(self, obj):
        return obj.modified_at


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'blog:post_list', 'stats']

    def location(self, item):
        return reverse(item)

