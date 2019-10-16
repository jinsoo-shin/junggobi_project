from django.conf.urls import url
from .api_views import test

urlpatterns = [
    url('index/$', test.index, name='index'),
]
