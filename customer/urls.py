from django.urls import path
from . import views


app_name = "customer"
urlpatterns = [   
  path('submit_enquiry/',views.event_enquiry, name='submit_enquiry'),
  ]