# Generated by Django 4.0.1 on 2022-02-21 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_remove_donor_firstname_remove_donor_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='donarAddress',
            new_name='donorAddress',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='donarDistrict',
            new_name='donorDistrict',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='donarDivision',
            new_name='donorDivision',
        ),
    ]
