# Generated by Django 5.1 on 2024-08-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_name',
            field=models.IntegerField(default=5),
        ),
    ]
