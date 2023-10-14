from rest_framework import serializers 
from .models import *
from django.core.validators import EmailValidator

'''
This class is for removing the timezone off the datetime field
'''
class RemoveTimeZone(serializers.DateTimeField):
    def to_representation(self, value):
        # Convert the DateTime object to a string without timezone information
        if value:
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return None
'''
email 
'''
class ShareNoteSerializer(serializers.Serializer):
    email = serializers.EmailField()
    pk = serializers.IntegerField()
'''
This is the note serializer
'''
class NoteSerializer(serializers.ModelSerializer):
    date_created = RemoveTimeZone()
    class Meta:
        model = Note
        fields = ('pk', 'title', 'body', 'date_created', 'category','due_date')