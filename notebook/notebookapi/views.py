from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated #ensure user is authenticated before they perform action
from rest_framework.authentication import *
#packages for filter,sort,order and search
# from django_filters import rest_framework as filters
# from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import *
from django.utils import timezone
#for sending email, creating csv and pdf
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from django.views.generic import View
import io
from django.conf import settings
from django.http import HttpResponse
import os
#email packages
from django.core.mail import EmailMessage
from django.http import JsonResponse
from .email import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .utils import *
import csv
# Create your views here.


'''enables us to accept GET requests to list all the notes available. 
It also allows us to accept POST requests to create a new note.'''

class NoteList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    # queryset = Note.objects.all()
    queryset = Note.objects.all().order_by('-date_created') #sorts all the notes list by the latest date future dates first(-) makes it negative
    serializer_class = NoteSerializer
    # filter_backends = [DjangoFilterBackend]
    filter_fields = ('category')
    search_fields =('category')
    #ordering notes
    ordering_fields = ( 
        'date_created', 
        # 'Overdue'
        #does not make sense to order by category when we are already filtering by category
        'category'   
    )
    #filtering notes
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = NoteFilter
    #searching notes
    search_fields = ['title']
    #due dates
    category = Note.objects.filter(date_created__lt=timezone.now(), category='overdue')
    
    

'''
responds to GET requests to provide the details of a specific note as indicated by the id or primary_key.
It also responds to PUT requests to update one or more of the fields of a tnote.
It also deletes a note instance when a DELETE request is made.
'''
class NoteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


'''
Export all the notes list to pdf and csv (5 points)
Share or publish the notes list over an email (5 points)
Set the email reminder for a note

'''




'''
Share or Publish Notes via Email:
'''
# permission_classes = [IsAuthenticated] 
# authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
# def send_notes_email(subject, message, to_email, attachment_path=None):
#     email = EmailMessage(subject, message, to=[to_email])

#     if attachment_path:
#         email.attach_file(attachment_path)

#     email.send()
# class ShareNotesEmailView(View):
#     permission_classes = [IsAuthenticated] 
#     authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
#     def post(self, request, *args, **kwargs):
#         # Retrieve notes and recipient email from request
#         notes = Note.objects.all()
#         recipient_email = request.data.get('recipient_email')

#         # Generate PDF or CSV file
#         attachment_path = self.generate_pdf_or_csv(notes)  # Replace with actual code

#         # Send the email
#         send_notes_email("Notes", "Here are your notes.", recipient_email, attachment_path)

#         return JsonResponse({'message': 'Email sent successfully'})

class ShareNotesEmailView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    def post(self, request):
        # # Retrieve the data you want to share
        # notes = Note.objects.all()
        # serializer = NoteSerializer(notes, many=True)
        # note_data = serializer.data

        # # Get the recipient's email address from the request
        # to_email = request.data.get('email')

        # # Send the email
        # send_note_data_email(to_email, str(note_data))

        # return Response({'message': 'note data shared via email successfully'})
        
        recipient_email = request.data.get('recipient_email')
        subject = "Your Note Data"
        
        # Query your Note model to get the data you want to share
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        message = "\n".join([f"{note['title']}: {note['content']}" for note in serializer.data])
        
        try:
            send_note_data_email(recipient_email, subject, message)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Email could not be sent'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

#generating pdf and csv
'''
generate PDF and CSV files of your notes.  create a PDF export view:
'''

class GeneratePDFView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="note_list.pdf"'

        p = canvas.Canvas(response)
        notes = Note.objects.all()
        for note in notes:
            p.drawString(100, 700, f"Title: {note.title}")
            p.drawString(100, 680, f"Content: {note.body}")
            p.drawString(100, 660, f"date_created: {note.date_created}")
            p.drawString(100, 640, f"category: {note.category}")
            p.showPage()
        p.save()

        return response

class GenerateCSVView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="note_list.csv"'

        writer = csv.writer(response)
        writer.writerow(['Title', 'Content','Date','Category'])
        notes = Note.objects.all()
        for note in notes:
            writer.writerow([note.title, note.body, note.date_created, note.category])

        return response






