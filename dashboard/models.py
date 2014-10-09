from django.db import models

# Create your models here.

class Alerts(models.Model):

	ticket_state = (
		('new','new'),
		('created','created'),
		('updated','updated'),
	)

	alert_state = (
		('clear','clear'),
		('info','info'),
		('warning','warning'),
		('critical','critical'),
		('major','major'),
	)

	ticket_status = models.CharField(max_length=10, choices=ticket_state)
	monitoring_server_name = models.CharField(max_length=255)
	alert_hostname = models.CharField(max_length=255)
	alert_name = models.CharField(max_length=255)
	alert_status = models.CharField(max_length=10, choices=alert_state)
	alert_detail = models.TextField()
	time = models.TimeField(auto_now=True, auto_now_add=True)
	date = models.DateField(auto_now=True, auto_now_add=True)
      
	jira_ticket = models.CharField(max_length=255, blank=True)
	jira_time = models.TimeField(null=True, blank=True)
	jira_date = models.DateField(null=True, blank=True)
        
	class Meta:
		get_latest_by = 'id'

