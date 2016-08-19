from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Post, Category, Tag
from django.utils import timezone


class PostListView(ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'post_list'
        context['query'] = self.request.GET.get('q')
        context['now'] = timezone.now()
        context['page'] = 'blog'

        return context

    def get_queryset(self):
        now = timezone.now()
        qs = super(PostListView, self).get_queryset()
        qs = qs.filter(published='published').filter(published_time__lte=now)
        query = self.request.GET.get('q')
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tag__title__icontains=query) |
                Q(category__title__icontains=query) |
                Q(user__userprofile__full_name__icontains=query)
            )

        return qs


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'single'
        context['query'] = self.request.GET.get('q')
        context['page'] = 'blog'

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
            )

        return qs


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_tag.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'category'
        context['now'] = timezone.now()
        context['query'] = self.request.GET.get('q')
        context['page'] = 'blog'

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
            )

        return qs


class TagDetailView(DetailView):
    model = Tag
    template_name = 'blog/category_tag.html'

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['page_type'] = 'tag'
        context['now'] = timezone.now()
        context['query'] = self.request.GET.get('q')
        context['page'] = 'blog'

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
