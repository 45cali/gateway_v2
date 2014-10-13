from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest import apiviews
from rest_framework.routers import DefaultRouter, SimpleRouter
from dashboard import views


admin.autodiscover()

router = DefaultRouter()
router.register(r'get', apiviews.AlertsViewSet)
router.register(r'search', apiviews.SearchAlertsViewSet)
router.register(r'alerts', apiviews.CreateAlert)


urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
        

)
