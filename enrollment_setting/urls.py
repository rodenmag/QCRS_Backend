__author__ = 'Roden Magat'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import *
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
from .models import *
from enrollment_setting import views




urlpatterns = format_suffix_patterns([
    url(r'^enrollment_setting_list/$', views.EnrollmentSettingCrudViewSet.as_view({ 'get': 'list' }), name='enrollment_setting-list'),
    url(r'^enrollment_setting_create/$', views.EnrollmentSettingCrudViewSet.as_view({ 'post': 'create' }), name='enrollment_setting-create'),
    url(r'^enrollment_setting_update/(?P<pk>.+)/$', views.EnrollmentSettingCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='enrollment_setting-put'),
    url(r'^enrollment_setting_delete/(?P<pk>.+)/$', views.EnrollmentSettingCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='enrollment_setting-delete'),
    url('enrollment_setting_filter/', EnrollmentSettingFilterView.as_view()),
])

urlpatterns += [
    url(r'^enrollment_setting/', include(router.urls)),
]