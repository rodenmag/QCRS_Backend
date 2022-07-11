__author__ = 'Roden Magat'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import *
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from .models import *
from enrollment_management import views

urlpatterns = format_suffix_patterns([
    url(r'^enrollment_list/$', views.EnrollmentCrudViewSet.as_view({ 'get': 'list' }), name='enrollment-list'),
    url(r'^enrollment_create/$', views.EnrollmentCrudViewSet.as_view({ 'post': 'create' }), name='enrollment-create'),
    url(r'^enrollment_update/(?P<pk>.+)/$', views.EnrollmentCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='enrollment-put'),
    url(r'^enrollment_delete/(?P<pk>.+)/$', views.EnrollmentCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='enrollment-delete'),
    url('enrollment_filter/', EnrollmentFilterView.as_view()),
])

urlpatterns += [
    url(r'^enrollment_management/', include(router.urls)),
]