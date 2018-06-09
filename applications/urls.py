# -*- coding: utf-8 -*-

"""URLs for Main Application"""

from django.conf.urls import url

from .views import ApplyView, ApplicationView, LoginView, ListApplicationView

urlpatterns = [
    url(r'^$', ApplyView.as_view(), name='apply'),
    url('^login/?$', LoginView.as_view(), name='login'),
    url(r'^application/(?P<applicationid>[A-Z0-9]{16})$', ApplicationView.as_view(), name='application'),
    url(r'^all/?$', ListApplicationView.as_view(), name='all'),
]