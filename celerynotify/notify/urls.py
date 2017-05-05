from django.conf.urls import url, include
from notify.views import NotifyView


urlpatterns = [
	url(r'^notify/$', NotifyView.as_view()),
]