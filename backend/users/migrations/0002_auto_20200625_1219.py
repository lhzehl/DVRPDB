# Generated by Django 3.0.3 on 2020-06-25 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Profile image')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last name')),
                ('username', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Username')),
                ('dob', models.DateTimeField(blank=True, null=True, verbose_name='Date of birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
