from django.shortcuts import render
from rest.serializer import AlertSerializer
from dashboard.models import Alerts
import django_filters
from rest_framework import viewsets, filters
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

class AlertFilter(django_filters.FilterSet):
	class Meta:
		model = Alerts
		fields = ['ticket_status', 
			'monitoring_server_name', 
			'alert_hostname', 
			'alert_name', 
			'alert_status',
			'alert_detail',
			'time',
			'date',
			'jira_ticket',
			'jira_time',
			'jira_date']

class AlertsViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Alerts.objects.all()
	serializer_class = AlertSerializer
	filter_class = AlertFilter

class SearchAlertsViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Alerts.objects.all()
	serializer_class = AlertSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('ticket_status', 
			'monitoring_server_name', 
			'alert_hostname', 
			'alert_name', 
			'alert_status',
			'alert_detail',
			'time',
			'date',
			'jira_ticket',
			'jira_time',
			'jira_date'
			)



class CreateAlert(viewsets.ModelViewSet):
	queryset = Alerts.objects.all()
	serializer_class = AlertSerializer
	filter_class = AlertFilter

