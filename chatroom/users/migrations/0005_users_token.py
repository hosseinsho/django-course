# Generated by Django 3.0.1 on 2020-02-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200222_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.UUIDField(null=True),
        ),
    ]