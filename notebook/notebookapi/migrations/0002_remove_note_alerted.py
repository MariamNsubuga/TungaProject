# Generated by Django 4.1.7 on 2023-10-22 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebookapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='alerted',
        ),
    ]
