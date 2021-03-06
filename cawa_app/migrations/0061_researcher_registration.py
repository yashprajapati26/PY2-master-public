# Generated by Django 2.2 on 2021-03-06 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cawa_app', '0060_delete_researcher_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher_registration',
            fields=[
                ('Registraion_number', models.AutoField(primary_key=True, serialize=False)),
                ('Conference_Theme', models.CharField(choices=[('Strategic Management', 'Strategic Management'), ('Accounting & Finance', 'Accounting & Finance'), ('Marketing', 'Marketing'), ('Human Resource Management', 'Human Resource Management'), ('Enterpreneueship and Innovations', 'Enterpreneueship and Innovations'), ('IT', 'IT')], max_length=100)),
                ('Institute', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=150)),
                ('Designation', models.CharField(max_length=50)),
                ('Members', models.CharField(default=1, max_length=10)),
                ('co_authors', models.CharField(default=' ', max_length=100)),
                ('Total_amount', models.IntegerField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.RegCategory')),
                ('Researcher_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cawa_app.Researcher')),
            ],
        ),
    ]
