# Generated by Django 5.1b1 on 2024-07-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
