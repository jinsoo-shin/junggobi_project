from django.conf.urls import url
from .api_views import product_views,search_views

urlpatterns = [
    # url('index/$', test.index, name='index'),
    url("product/$", product_views.information, name="product_info"),
    url("search/$", search_views.search, name="search"),
    url("auto/$", search_views.auto, name="auto"),
]
