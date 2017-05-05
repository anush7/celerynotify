from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.contrib.auth.models import User
from gcm import GCM

API_KEY = 'Your-Api-Key'
gcm = GCM(API_KEY)


@shared_task
def notify_users(msg_title, msg_body, conditional_clause):
	reg_ids = User.objects.values_list('gcm_id',flat=True) #assuming gcm id is stored in gcm_id field
	data = {
		'message_title': msg_title,
		'message_body': msg_body,
		'conditional_clause': conditional_clause
	}
	gcm.json_request(registration_ids=reg_ids, data=data)