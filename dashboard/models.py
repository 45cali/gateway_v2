from django.db import models

# Create your models here.

class Alerts(models.Model):

	ticket_state = (
		(0,'new'),
		(1,'created'),
		(2,'updated'),
	)

	alert_state = (
		(0,'clear'),
		(1,'info'),
		(2,'warning'),
		(3,'critical'),
		(4,'major'),
	)

	ticket_status = models.IntegerField(max_length=1, choices=ticket_state)
	monitoring_server_name = models.CharField(max_length=255)
	alert_hostname = models.CharField(max_length=255)
	alert_name = models.CharField(max_length=255)
	alert_status = models.IntegerField(max_length=1, choices=alert_state)
	alert_detail = models.TextField()
	time = models.TimeField(auto_now=True, auto_now_add=True)
	date = models.DateField(auto_now=True, auto_now_add=True)
      
	jira_ticket = models.CharField(max_length=255)
	jira_time = models.TimeField(required=False)
	jira_date = models.DateField(required=False)
        
	class Meta:
		get_latest_by = 'id'

