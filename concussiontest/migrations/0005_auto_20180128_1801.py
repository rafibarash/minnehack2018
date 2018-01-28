# Generated by Django 2.0.1 on 2018-01-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concussiontest', '0004_auto_20180128_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='name',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='slug',
        ),
        migrations.AddField(
            model_name='athlete',
            name='first',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='athlete',
            name='last',
            field=models.CharField(default='', max_length=15),
        ),
    ]
