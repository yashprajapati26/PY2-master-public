# Generated by Django 2.0 on 2021-01-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0016_auto_20210127_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='Phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='Phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='Phone',
            field=models.BigIntegerField(),
        ),
    ]
