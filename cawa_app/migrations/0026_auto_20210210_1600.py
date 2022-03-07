# Generated by Django 2.0 on 2021-02-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0025_conference'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Conference',
        ),
        migrations.AlterField(
            model_name='participant',
            name='About',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='Address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='About',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='Address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='About',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='Address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]