from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest import apiviews
from rest_framework.routers import DefaultRouter
from dashboard import views
from django.shortcuts import redirect


router = DefaultRouter()
router.register(r'get', apiviews.AlertsViewSet)
router.register(r'search', apiviews.SearchAlertsViewSet)
router.register(r'create', apiviews.CreateAlert)


urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^', views.index, name='index'),
    url(r'^#/api/get$', views.apiRedirect),
    url(r'^#/login', views.loginRedirect),
    

)
