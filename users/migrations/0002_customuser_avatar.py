# Generated by Django 3.0.1 on 2020-07-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='/media/avatars/avatar.png', null=True, upload_to='avatars/'),
        ),
    ]
