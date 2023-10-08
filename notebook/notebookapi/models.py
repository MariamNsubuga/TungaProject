from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Note(models.Model):
    title =models.CharField(max_length =100)
    body =models.CharField(max_length =100)
    date_created =models.DateTimeField(blank=True, null=True,default="datetime.date.today")
    category = models.CharField(max_length=100)
    

    def __str__(self) :  #returns the title of the note
        return self.title 
