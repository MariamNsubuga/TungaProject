from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
   

    path('', NoteList.as_view()),
    path('/<int:pk>', NoteDetail.as_view()),
    path('/pdf', GeneratePDFView.as_view()),
    path('/csv', GenerateCSVView.as_view()),
    path('/excel/', GenerateExcelView.as_view()),
    path('/email', send_notes_via_email, name='send-notes-via-email'),
    
    
]





