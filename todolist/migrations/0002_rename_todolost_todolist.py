# Generated by Django 5.1.6 on 2025-03-05 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todolost',
            new_name='Todolist',
        ),
    ]
