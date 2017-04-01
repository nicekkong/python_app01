from django.conf.urls import url
from nicekkong import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insert$', views.insert, name='insert')
]
