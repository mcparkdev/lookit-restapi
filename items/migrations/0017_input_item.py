# Generated by Django 3.0.7 on 2020-06-29 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0016_auto_20200628_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=100)),
                ('store', models.CharField(blank=True, max_length=100)),
                ('message', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=15)),
                ('link', models.CharField(max_length=1000)),
                ('store', models.CharField(max_length=100)),
                ('imageURL', models.CharField(max_length=1000)),
                ('logo', models.CharField(max_length=1000)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Input')),
            ],
        ),
    ]
