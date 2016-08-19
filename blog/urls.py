from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import PostListView, PostDetailView, CategoryDetailView, TagDetailView

urlpatterns = [
    url(r'^posts/$', login_required(PostListView.as_view()), name='post_list'),
    url(r'^posts/(?P<slug>[\w-]+)/$', login_required(PostDetailView.as_view()), name='post_detail'),
    url(r'^posts/category/(?P<slug>[\w-]+)/$', login_required(CategoryDetailView.as_view()), name='category_detail'),
    url(r'^posts/tag/(?P<slug>[\w-]+)/$', login_required(TagDetailView.as_view()), name='tag_detail'),
]