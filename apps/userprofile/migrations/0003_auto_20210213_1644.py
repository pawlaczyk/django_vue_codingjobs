# Generated by Django 3.1.6 on 2021-02-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_conversationmessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='creatd_by',
            new_name='created_by',
        ),
    ]
