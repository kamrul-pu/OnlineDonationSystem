# Generated by Django 4.0.1 on 2022-02-21 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_alter_donor_profile_pic_alter_volunteer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='Name',
        ),
    ]