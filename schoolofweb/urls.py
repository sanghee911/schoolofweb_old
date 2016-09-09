from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap, StaticViewSitemap


sitemaps = {
    'blog': BlogSitemap,
    'static': StaticViewSitemap,
}


urlpatterns = [
    # django
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # sites
    url(r'', include('common.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # thirth-party
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'common.views.custom_404'
