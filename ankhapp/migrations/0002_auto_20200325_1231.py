# Generated by Django 3.0.4 on 2020-03-25 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ankhapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
