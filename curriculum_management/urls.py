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
from curriculum_management import views




urlpatterns = format_suffix_patterns([
    url(r'^curriculum_list/$', views.CurriculumCrudViewSet.as_view({ 'get': 'list' }), name='curriculum-list'),
    url(r'^curriculum_create/$', views.CurriculumCrudViewSet.as_view({ 'post': 'create' }), name='curriculum-create'),
    url(r'^curriculum_update/(?P<pk>.+)/$', views.CurriculumCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='curriculum-put'),
    url(r'^curriculum_delete/(?P<pk>.+)/$', views.CurriculumCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='curriculum-delete'),
    url('curriculum_filter/', CurriculumFilterView.as_view()),

    url(r'^curriculum_content_list/$', views.CurriculumContentCrudViewSet.as_view({ 'get': 'list' }), name='curriculum_content-list'),
    url(r'^curriculum_content_create/$', views.CurriculumContentCrudViewSet.as_view({ 'post': 'create' }), name='curriculum_content-create'),
    url(r'^curriculum_content_update/(?P<pk>.+)/$', views.CurriculumContentCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='curriculum_content-put'),
    url(r'^curriculum_content_delete/(?P<pk>.+)/$', views.CurriculumContentCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='curriculum_content-delete'),
    url('curriculum_content_filter/', CurriculumContentFilterView.as_view()),
])

urlpatterns += [
    url(r'^curriculum_management/', include(router.urls)),
]