# Generated by Django 2.0 on 2021-03-12 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0071_auto_20210312_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Conference_Theme', models.CharField(choices=[('Strategic Management', 'Strategic Management'), ('Accounting & Finance', 'Accounting & Finance'), ('Marketing', 'Marketing'), ('Human Resource Management', 'Human Resource Management'), ('Enterpreneueship and Innovations', 'Enterpreneueship and Innovations'), ('IT', 'IT')], max_length=100)),
                ('Institute', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=150)),
                ('Designation', models.CharField(max_length=50)),
                ('Amount', models.IntegerField()),
                ('Payment_status', models.BooleanField(default=False)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.RegCategory')),
                ('Participant_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.Participant')),
            ],
        ),
    ]
