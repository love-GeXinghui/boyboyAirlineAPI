# Generated by Django 4.1.7 on 2023-05-09 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("airline", "0003_alter_passenger_table"),
    ]

    operations = [
        migrations.DeleteModel(name="join",),
    ]
