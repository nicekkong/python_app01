from django.conf.urls import url
from lotto import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post, name="new_lotto"),
    url(r'^(?P<lottoKey>[0-9]+)/detail/$', views.detail, name="detail"),
]


