# Generated by Django 3.0.7 on 2020-06-28 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_remove_input_input'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Input',
        ),
    ]
