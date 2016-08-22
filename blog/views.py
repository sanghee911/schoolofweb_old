# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.utils import timezone
from hitcount.views import HitCountDetailView
from .models import Post, Category, Tag


class PostListView(ListView):
    model = Post
    paginate_by = 5

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
        queries_without_page = self.request.GET.copy()

        if 'page' in queries_without_page:
            del queries_without_page['page']
        context['queries'] = queries_without_page

        # meta content
        context['meta_title'] = 'Blog'
        context['meta_description'] = '웹 개발, 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.'
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
        context['meta_author'] = '이상희, Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context

    def get_queryset(self):
        qs = super(PostDetailView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tag__title__icontains=query) |
                Q(category__title__icontains=query) |
                Q(user__userprofile__full_name__icontains=query)
            ).distinct()

        return qs


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_tag.html'

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'category'
        context['now'] = timezone.now()
        context['query'] = self.request.GET.get('q')
        context['page'] = 'blog'

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
        context['meta_title'] = 'Blog'
        context['meta_description'] = '웹 개발, 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.'
        context['meta_keywords'] = '무료 인터넷 강좌, 파이썬, 장고, 리눅스, Python, Django, Linux'
        context['meta_author'] = '이상희, Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context

    def get_queryset(self):
        qs = super(CategoryDetailView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tag__title__icontains=query) |
                Q(category__title__icontains=query) |
                Q(user__userprofile__full_name__icontains=query)
            ).distinct()

        return qs


class TagDetailView(DetailView):
    model = Tag
    template_name = 'blog/category_tag.html'

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'tag'
        context['now'] = timezone.now()
        context['query'] = self.request.GET.get('q')
        context['page'] = 'blog'

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
        context['meta_title'] = 'Blog'
        context['meta_description'] = '웹 개발, 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.'
        context['meta_keywords'] = '무료 인터넷 강좌, 파이썬, 장고, 리눅스, Python, Django, Linux'
        context['meta_author'] = '이상희, Sanghee Lee'
        context['meta_url'] = self.request.build_absolute_uri

        return context

    def get_queryset(self):
        qs = super(TagDetailView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tag__title__icontains=query) |
                Q(category__title__icontains=query) |
                Q(user__userprofile__full_name__icontains=query)
            )

        return qs
