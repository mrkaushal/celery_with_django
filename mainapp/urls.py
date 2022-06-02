from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.test, name='test'),
    path('sendmail', views.send_mail_to_all, name='sendmail'),
]
