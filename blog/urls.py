from django.conf.urls import url
from .views import PostListView, PostDetailView, CatTagListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^posts/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^posts/category/(?P<slug>[\w-]+)/$', CatTagListView.as_view(), name='category_list'),
    url(r'^posts/tag/(?P<slug>[\w-]+)/$', CatTagListView.as_view(), name='tag_list'),
]
