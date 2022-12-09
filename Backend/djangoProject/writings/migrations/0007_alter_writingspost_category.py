# Generated by Django 4.0.5 on 2022-10-25 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0006_alter_writingspost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writingspost',
            name='category',
            field=models.CharField(choices=[('Nutrition', 'Nutrition'), ('Disease', 'Disease'), ('Beauty', 'Beauty')], default='Nutrition', max_length=50),
        ),
    ]