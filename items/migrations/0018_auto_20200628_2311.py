# Generated by Django 3.0.7 on 2020-06-29 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_input_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='message',
        ),
        migrations.RemoveField(
            model_name='input',
            name='store',
        ),
    ]
