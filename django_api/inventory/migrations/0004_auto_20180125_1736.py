# Generated by Django 2.0.1 on 2018-01-25 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20180116_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='datetime',
        ),
        migrations.AddField(
            model_name='complain',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
