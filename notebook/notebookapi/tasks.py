
from celery import shared_task
from django.utils import timezone
from .models import Note
from django.core.mail import send_mail
import os
# import logging

@shared_task
def send_reminders():
    current_time = timezone.now()
    # Define the time frame for "almost due" notes, for example, within 24 hours
    time_frame = current_time + timezone.timedelta(days=1)
    # Retrieve notes with due dates within the time frame
    notes = Note.objects.filter(due_date__gt=current_time, due_date__lt=time_frame)

    
   

    for note in notes:
        subject = f'Reminder by celery for notebook: {note.title}'
        message = f'Reminder for the note: {note.body}\nDue Date: {note.due_date}'
        from_email = 'mariamtestn@gmail.com'  
        recipient_list = [note.user.email]  
        # recipient_list = ['mariam.nakanyike01@gmail.com'] 
        # Log email details for debugging
        # logger.info(f"Sending email to {recipient_list} with subject: {subject}")

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        # Mark the note as a reminder sent to avoid duplicate reminders
        note.is_reminder_sent = True
        note.save()
