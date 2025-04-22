#
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/foobar/myproject/
pythonpath = ..
env = DJANGO_SETTINGS_MODULE=myproject.settings
module = django.core.handlers.wsgi:WSGIHandler()
processes = 4
threads = 2
stats = 127.0.0.1:9191

