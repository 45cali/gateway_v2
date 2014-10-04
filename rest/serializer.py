from rest_framework import serializers
from dashboard.models import Alerts

class AlertSerializer(serializers.ModelSerializer):
	class Meta:
        	model = Alerts
       		fields = ('id',
			'ticket_status', 
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


