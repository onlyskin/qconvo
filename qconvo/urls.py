from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^exchange/', include('exchange.urls')),
    url(r'^admin/', admin.site.urls),
]
