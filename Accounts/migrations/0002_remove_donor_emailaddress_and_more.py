# Generated by Django 4.0.1 on 2022-02-21 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='emailAddress',
        ),
    ]
