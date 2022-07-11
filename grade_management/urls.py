__author__ = 'Roden Magat'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import *
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
from .models import *
from grade_management import views




urlpatterns = format_suffix_patterns([
    url(r'^grades_list/$', views.GradesCrudViewSet.as_view({ 'get': 'list' }), name='grades-list'),
    url(r'^grades_create/$', views.GradesCrudViewSet.as_view({ 'post': 'create' }), name='grades-create'),
    url(r'^grades_update/(?P<pk>.+)/$', views.GradesCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='grades-put'),
    url(r'^grades_delete/(?P<pk>.+)/$', views.GradesCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='grades-delete'),
    url('grades_filter/', GradesFilterView.as_view()),
    url('evaluation/', EvaluationFilterView.as_view()),
])

urlpatterns += [
    url(r'^grade_management/', include(router.urls)),
]