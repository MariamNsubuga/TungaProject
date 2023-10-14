from django.db import models
# from django.contrib.auth.models import User 
from django.conf import settings
from datetime import datetime
# Create your models here.

class Note(models.Model):
    title =models.CharField(max_length =100)
    body =models.CharField(max_length =100)
    date_created =models.DateTimeField(blank=True, null=True,default="datetime.date.today")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # due_date = datetime.now()
    due_date = models.DateTimeField(blank=True, null=True,default="datetime.date.today")
    # category = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
        ('unfinished', 'Unfinished'),
        ('overdue', 'Overdue'),
        ('done','Done')
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='done')
    

    def __str__(self) :  #returns the title of the note
        return self.title 

