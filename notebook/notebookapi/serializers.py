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
        fields = ('pk', 'title', 'body', 'date_created', 'category','due_date','email_reminder','reminder')
   

        # def update(self, instance, validated_data):
        # Check if due_date is changed or other conditions for alert are no longer met
            # if instance.due_date != validated_data.get('due_date'):
            #     instance.alerted = False  # Note no longer requires alert
            # instance.title = validated_data.get('title', instance.title)
            # instance.body = validated_data.get('body', instance.content)
            # instance.due_date = validated_data.get('due_date', instance.due_date)
            # instance.save()
            # return instance