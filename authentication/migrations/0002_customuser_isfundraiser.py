# Generated by Django 4.2.2 on 2023-06-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isFundraiser',
            field=models.BooleanField(default=False),
        ),
    ]
