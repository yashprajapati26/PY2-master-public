# Generated by Django 2.2 on 2021-02-20 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0042_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=20)),
                ('Amount', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='participant_registration',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.RegCategory'),
        ),
    ]
