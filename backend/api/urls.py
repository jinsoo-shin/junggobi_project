from django.conf.urls import url
from .api_views import test, product_views

urlpatterns = [
    # url('index/$', test.index, name='index'),
    url("product/$", product_views.information, name="product_info")
]
