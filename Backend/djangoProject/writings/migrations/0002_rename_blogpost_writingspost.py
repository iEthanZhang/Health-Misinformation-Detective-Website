# Generated by Django 4.0.5 on 2022-10-16 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='WritingsPost',
        ),
    ]
