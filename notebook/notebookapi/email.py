from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated #ensure user is authenticated before they perform action
from rest_framework.authentication import *

from django.core.mail import EmailMessage

# def send_blog_data_email(to_email, blog_data):
#     subject = "Blog Data"
#     message = "Here is the latest blog data:\n\n" + blog_data

#     email = EmailMessage(subject, message, to=[to_email])
#     email.send()

from django.core.mail import send_mail
permission_classes = [IsAuthenticated] 
authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
def send_note_data_email(recipient_email, subject, message):
    send_mail(subject, message, from_email=None, recipient_list=[recipient_email])