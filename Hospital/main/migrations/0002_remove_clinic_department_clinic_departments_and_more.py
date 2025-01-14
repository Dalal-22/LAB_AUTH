# Generated by Django 4.1.7 on 2023-02-19 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='department',
        ),
        migrations.AddField(
            model_name='clinic',
            name='departments',
            field=models.CharField(choices=[('HC', 'HeartCenter'), ('NC', 'NeuroscienceCenter'), ('OC', 'ObesityCenter'), ('EC', 'EyeCenter'), ('OcC', 'OrthopedicCenter')], default='NL', max_length=3),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=models.CharField(max_length=512),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_description', models.TextField()),
                ('patient_age', models.IntegerField()),
                ('appointment_datetime', models.DateTimeField()),
                ('is_attended', models.BooleanField(default=False)),
                ('apclinec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clinic')),
                ('appointmentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
