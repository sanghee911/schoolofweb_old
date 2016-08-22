from django.conf.urls import url
from .views import PostListView, PostDetailView, CategoryDetailView, TagDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^posts/$', PostListView.as_view(), name='post_list'),
    url(r'^posts/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^posts/category/(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
    url(r'^posts/tag/(?P<slug>[\w-]+)/$', TagDetailView.as_view(), name='tag_detail'),
]
