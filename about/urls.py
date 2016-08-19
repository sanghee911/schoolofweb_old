from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import about

urlpatterns = [
    url(r'', about, name='about'),
]
