# Generated by Django 2.0 on 2021-03-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0072_participant_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant_registration',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='participant_registration',
            name='Participant_users',
        ),
        migrations.DeleteModel(
            name='Participant_registration',
        ),
    ]