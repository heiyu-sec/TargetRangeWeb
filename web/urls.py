#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:blackfeather
from django.conf.urls import url,include
from web.views import account
from web.views  import home
from web.views  import project,manage

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^image/code/$', account.image_code, name='image_code'),
    url(r'^index/$', home.index, name='index'),
    url(r'^logout/$', account.logout, name='logout'),

    #项目列表
    url(r'^project/list/$', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    url(r'^project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar, name='project_unstar'),

    #项目管理
    url(r'^manage/(?P<project_id>\d+)/', include([
        url(r'^dashboard/$', manage.dashboard, name='dashboard'),
        url(r'^issues/$', manage.issues, name='issues'),
        url(r'^statistics/$', manage.statistics, name='statistics'),
        url(r'^file/$', manage.file, name='file'),
        url(r'^wiki/$', manage.wiki, name='wiki'),
        url(r'^setting/$', manage.setting, name='setting'),
    ], None, None)),

]