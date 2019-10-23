from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('search/', include('haystack.urls')),
    url(r'^search/', include('haystack.urls')),


]
