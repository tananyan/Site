from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^news/', include('NewsApp.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^registration/$', views.registration, name='registration'),
]