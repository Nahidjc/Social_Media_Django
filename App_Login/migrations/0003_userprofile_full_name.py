# Generated by Django 3.1.5 on 2021-06-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
