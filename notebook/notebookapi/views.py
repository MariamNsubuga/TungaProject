from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated #ensure user is authenticated before they perform action
# Create your views here.


'''enables us to accept GET requests to list all the notes available. 
It also allows us to accept POST requests to create a new note.'''

class NoteList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

'''
responds to GET requests to provide the details of a specific note as indicated by the id or primary_key.
It also responds to PUT requests to update one or more of the fields of a tnote.
It also deletes a note instance when a DELETE request is made.
'''
class NoteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Note.objects.all()
    serializer_class = NoteSerializer