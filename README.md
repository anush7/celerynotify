# celerynotify

notify users at specific scheduled time using celery and google cloud messaging.

### Usage:

make a post request to this url using below data
```
http://127.0.0.1:8000/api/notify/
```

post data: 

```
data = {
"message_title":"title",
"message_body":"body",
"conditional_clause":"true",
"date_time":"05/05/2017 09:42PM"
}
```

### Requirements:
```
Django==1.8.18
djangorestframework==3.6.2
celery==4.0.2
python-gcm==0.4
```
