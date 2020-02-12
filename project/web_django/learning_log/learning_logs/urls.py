#!/usr/bin/env/python3

"""定义learning_logs的URL模式"""

from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index),
    path('topics/', views.topics, name='topics'),
    path(r'^topics/(?P<topic_Id>\d+)/$', views.topics, name='topic'),
]


