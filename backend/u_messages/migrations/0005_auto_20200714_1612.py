# Generated by Django 3.0.3 on 2020-07-14 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('u_messages', '0004_auto_20200714_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='dialog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='u_messages.Dialog', verbose_name='Dialog'),
        ),
    ]