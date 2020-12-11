"""Defines URL patterns for Learning_logs."""

from django.urls import path, re_path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
