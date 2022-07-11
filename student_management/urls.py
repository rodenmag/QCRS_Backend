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
from student_management import views




urlpatterns = format_suffix_patterns([
    url(r'^student_balance_list/$', views.StudentBalanceViewSet.as_view({ 'get': 'list' }), name='student-balance-list'),
    url(r'^student_list/$', views.StudentCrudViewSet.as_view({ 'get': 'list' }), name='student-list'),
    url(r'^student_create/$', views.StudentCrudViewSet.as_view({ 'post': 'create' }), name='student-create'),
    url(r'^student_update/(?P<pk>.+)/$', views.StudentCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='student-put'),
    url(r'^student_delete/(?P<pk>.+)/$', views.StudentCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='student-delete'),
    url('student_filter/', StudentFilterView.as_view()),
])

urlpatterns += [
    url(r'^student_management/', include(router.urls)),
]