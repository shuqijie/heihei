from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index/(\d*)$', views.index),
    url(r'^write/$', views.write),
    url(r'^mysearch/$', views.mysearch),
]