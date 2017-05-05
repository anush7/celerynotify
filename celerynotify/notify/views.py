import pytz
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from notify.tasks import notify_users


class NotifyView(APIView):

	def post(self, request):
		msg_title = request.data["message_title"]
		msg_body = request.data["message_body"]
		conditional_clause = request.data["conditional_clause"]
		date_time = request.data["date_time"]

		schedule_time = datetime.strptime(date_time, '%m/%d/%Y %I:%M%p')
		ind_tzone = pytz.timezone('Asia/Kolkata')
		ind_schedule_time = ind_tzone.localize(schedule_time, is_dst=None)

		utc_tzone = pytz.utc
		utc_schedule_time = ind_schedule_time.astimezone(utc_tzone)

		notify_users.apply_async((msg_title, msg_body, conditional_clause), eta=utc_schedule_time)

		return Response({'success':'notification scheduled'}, status=status.HTTP_200_OK)