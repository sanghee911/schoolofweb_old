from django.conf.urls import url
from .views import StatView


urlpatterns = [
    url(r'^$', StatView.as_view(), name='stats'),
]