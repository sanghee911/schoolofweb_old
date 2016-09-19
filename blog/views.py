# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.db.models import Q
from django.utils import timezone
from hitcount.views import HitCountDetailView
from .models import Post, Category, Tag


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super(PostListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['category_post'] = []
        for category in context['category_list']:
            if self.request.user.is_superuser:
                category_post = category.category_post.all()
            else:
                category_post = category.category_post.filter(published='published').filter(published_time__lte=now)
            category_post_count = category_post.count()
            context['category_post'].append((category, category_post_count))

        context['tag_list'] = Tag.objects.all()
        context['tag_post'] = []
        for tag in context['tag_list']:
            if self.request.user.is_superuser:
                tag_post = tag.tag_post.all()
            else:
                tag_post = tag.tag_post.filter(published='published').filter(published_time__lte=now)
            tag_post_count = tag_post.count()
            context['tag_post'].append((tag, tag_post_count))

        context['page_type'] = 'post_list'
        context['query'] = self.request.GET.get('q')
        context['now'] = timezone.now()
        context['page'] = 'blog'
        context['recent_updates'] = Post.objects \
                                        .filter(published='published') \
                                        .filter(published_time__lte=now)[:5]
        queries_without_page = self.request.GET.copy()

        if 'page' in queries_without_page:
            del queries_without_page['page']
        context['queries'] = queries_without_page

        # meta content
        context['meta_title'] = 'Blog'
        context['meta_description'] = '웹 개발, 파이썬, 장고, 리눅스 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.'
        context['meta_keywords'] = '무료 인터넷 강좌, 파이썬, 장고, 리눅스, Python, Django, Linux'
        context['meta_author'] = '이상희, Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context

    def get_queryset(self):
        now = timezone.now()
        qs = super(PostListView, self).get_queryset()

        if not self.request.user.is_superuser:
            qs = qs.filter(published='published').filter(published_time__lte=now)
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tag__title__icontains=query) |
                Q(category__title__icontains=query) |
                Q(user__userprofile__full_name__icontains=query)
            ).distinct()

        return qs


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'single'
        context['query'] = self.request.GET.get('q')
        context['page'] = 'blog'
        context['recent_updates'] = Post.objects \
                                        .filter(published='published') \
                                        .filter(published_time__lte=now)[:5]
        context['category_post'] = []
        for category in context['category_list']:
            if self.request.user.is_superuser:
                category_post = category.category_post.all()
            else:
                category_post = category.category_post.filter(published='published').filter(published_time__lte=now)
            category_post_count = category_post.count()
            context['category_post'].append((category, category_post_count))

        context['tag_post'] = []
        for tag in context['tag_list']:
            if self.request.user.is_superuser:
                tag_post = tag.tag_post.all()
            else:
                tag_post = tag.tag_post.filter(published='published').filter(published_time__lte=now)
            tag_post_count = tag_post.count()
            context['tag_post'].append((tag, tag_post_count))

        # meta content
        context['meta_title'] = self.object.title
        context['meta_description'] = self.object.description
        context['meta_keywords'] = self.object.keywords
        context['meta_author'] = '이상희 Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context


class CatTagListView(ListView):
    model = Post
    template_name = 'blog/cat_tag_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super(CatTagListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        if '/blog/posts/category/' in self.request.path_info:
            context['page_type'] = 'category'
            context['category_title'] = Category.objects.get(slug=self.kwargs['slug']).title
        elif '/blog/posts/tag/' in self.request.path_info:
            context['page_type'] = 'tag'
            context['tag_title'] = Tag.objects.get(slug=self.kwargs['slug']).title
        context['now'] = timezone.now()
        context['page'] = 'blog'
        context['recent_updates'] = Post.objects \
                                        .filter(published='published') \
                                        .filter(published_time__lte=now)[:5]

        # make a list of tuples for category list in sidebar [('category_title', number_of_post), ...]
        context['category_post'] = []
        for category in context['category_list']:
            if self.request.user.is_superuser:
                category_post = category.category_post.all()
            else:
                category_post = category.category_post.filter(published='published').filter(published_time__lte=now)
            category_post_count = category_post.count()
            context['category_post'].append((category, category_post_count))

        # make a list of tuples for tag list in sidebar [('tag_title', number_of_post), ...]
        context['tag_post'] = []
        for tag in context['tag_list']:
            if self.request.user.is_superuser:
                tag_post = tag.tag_post.all()
            else:
                tag_post = tag.tag_post.filter(published='published').filter(published_time__lte=now)
            tag_post_count = tag_post.count()
            context['tag_post'].append((tag, tag_post_count))

        # meta content
        context['meta_title'] = 'Blog'
        context['meta_description'] = '웹 개발, 프로그래밍, 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.'
        context['meta_keywords'] = '무료 인터넷 강좌, 파이썬, 장고, 리눅스, Python, Django, Linux'
        context['meta_author'] = '이상희 Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context

    def get_queryset(self):
        now = timezone.now()
        qs = super(CatTagListView, self).get_queryset()

        if not self.request.user.is_superuser:
            qs = qs.filter(published='published').filter(published_time__lte=now)

        if '/blog/posts/category/' in self.request.path_info:
            qs = qs.filter(category__slug=self.kwargs['slug'])
        elif '/blog/posts/tag/' in self.request.path_info:
            qs = qs.filter(tag__slug=self.kwargs['slug'])

        return qs
