# Generated by Django 3.0.1 on 2020-07-31 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200731_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='AboutYou',
            field=models.TextField(blank=True, null=True),
        ),
    ]