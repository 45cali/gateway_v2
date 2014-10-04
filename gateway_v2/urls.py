from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'get', apiviews.AlertsViewSet)
router.register(r'search', apiviews.SearchAlertsViewSet)
router.register(r'create', apiviews.CreateAlert)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gateway_v2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
  #  url(r'^api/create', apiviews.create),
)
