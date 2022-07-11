__author__ = 'Roden Magat'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import *
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
from .models import *
from payment_management import views




urlpatterns = format_suffix_patterns([
    url(r'^payment_list/$', views.PaymentCrudViewSet.as_view({ 'get': 'list' }), name='payment-list'),
    url(r'^payment_create/$', views.PaymentCrudViewSet.as_view({ 'post': 'create' }), name='payment-create'),
    url(r'^payment_update/(?P<pk>.+)/$', views.PaymentCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='payment-put'),
    url(r'^payment_delete/(?P<pk>.+)/$', views.PaymentCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='payment-delete'),
    url('payment_filter/', PaymentFilterView.as_view()),

    
    url(r'^sponsor_balance_list/$', views.SponsorBalanceViewSet.as_view({ 'get': 'list' }), name='sponsor_balance-list'),
    url(r'^sponsor_payment_list/$', views.SponsorPaymentCrudViewSet.as_view({ 'get': 'list' }), name='sponsor_payment-list'),
    url(r'^sponsor_payment_create/$', views.SponsorPaymentCrudViewSet.as_view({ 'post': 'create' }), name='sponsor_payment-create'),
    url(r'^sponsor_payment_update/(?P<pk>.+)/$', views.SponsorPaymentCrudViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='sponsor_payment-put'),
    url(r'^sponsor_payment_delete/(?P<pk>.+)/$', views.SponsorPaymentCrudViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='sponsor_payment-delete'),
    url('sp_filter/', SponsorPaymentFilterView.as_view()),

    url(r'^sponsor_list/$', views.SponsorViewSet.as_view({ 'get': 'list' }), name='sponsor-list'),
    url(r'^sponsor_create/$', views.SponsorViewSet.as_view({ 'post': 'create' }), name='sponsor-create'),
    url(r'^sponsor_update/(?P<pk>.+)/$', views.SponsorViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update' }), name='sponsor-put'),
    url(r'^sponsor_delete/(?P<pk>.+)/$', views.SponsorViewSet.as_view({ 'get': 'retrieve', 'delete': 'destroy' }), name='sponsor-delete'),
])

urlpatterns += [
    url(r'^payment_management/', include(router.urls)),
]