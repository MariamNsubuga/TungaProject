# from django.core.mail import send_mail
# from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .models import Note

# def send_email_reminders():
#     now = datetime.now()
#     due_notes = Note.objects.filter(due_date__lte=now, reminder=True)
#     for note in due_notes:
#         send_mail(
#             'Reminder: ' + note.title,
#             note.body,
#             'mariamtestn@gmail.com',
#             [note.email],
#             fail_silently=False,
#         )

# def start_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(send_email_reminders, 'interval', minutes=2)
#     scheduler.start()
# utils.py
from django.core.mail import send_mail

def send_email_reminders():
    notes = Note.objects.filter(due_date__lt=timezone.now(), reminder=True)

    for note in notes:
        subject = 'Reminder: ' + note.title
        message = 'Your note "{}" is due.'.format(note.title)
        from_email = 'mariamtestn@gmail.com'
        recipient_list = [note.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
