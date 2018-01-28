# Generated by Django 2.0.1 on 2018-01-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('slug', models.SlugField(default='', unique=True)),
                ('base_time', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('new_time_1', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('new_time_2', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
    ]
