# Generated by Django 3.0.4 on 2020-03-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankhapp', '0004_auto_20200326_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetails',
            name='task_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
