# Generated by Django 4.2.2 on 2023-06-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jars', '0002_alter_jar_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='jar',
            name='monoJarid',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]
