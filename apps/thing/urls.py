from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add', views.add, name = 'add'),
    url(r'^create', views.create, name = 'create'),
    url(r'^join/(?P<trip_id>[0-9])', views.join, name = 'join'),
    url(r'^show/(?P<trip_id>[0-9])', views.show, name = 'show'),
]