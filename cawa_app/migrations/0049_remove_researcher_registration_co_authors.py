# Generated by Django 2.2 on 2021-03-03 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0048_auto_20210302_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher_registration',
            name='Co_authors',
        ),
    ]
