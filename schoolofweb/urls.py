from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include('common.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # thirth-party
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'common.views.custom_404'
