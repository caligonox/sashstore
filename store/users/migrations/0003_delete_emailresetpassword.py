# Generated by Django 4.0 on 2023-11-12 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailresetpassword'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailResetPassword',
        ),
    ]
