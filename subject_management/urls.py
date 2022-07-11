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
from subject_management import views




urlpatterns = format_suffix_patterns([
    url(r'^subject_list/$', views.SubjectCrudViewSet.as_view({ 'get': 'list' }), name='subject-list'),
    url(r'^subject_create/$', views.SubjectCrudViewSet.as_view({ 'post': 'create' }), name='subject-create'),
    url(r'^subject_update/(?P<pk>.+)/$', views.SubjectCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='subject-put'),
    url(r'^subject_delete/(?P<pk>.+)/$', views.SubjectCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='subject-delete'),
    url('subject_filter/', SubjectFilterView.as_view()),
])

urlpatterns += [
    url(r'^subject_management/', include(router.urls)),
]