from django.urls import path
from . import views


app_name = "owner"
urlpatterns = [   
   path('home/',views.home,name='home'),
   path('inner-page/',views.inner_page,name='inner-page'),
   


  ]
