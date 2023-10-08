from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
   

    path('', NoteList.as_view()),
    path('<int:pk>', NoteDetail.as_view()),
    
]




