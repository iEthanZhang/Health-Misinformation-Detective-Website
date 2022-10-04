# Generated by Django 4.1.1 on 2022-10-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_member_createdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='createDatetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Female'), (1, 'Male')], default=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(default='123456', max_length=16),
        ),
    ]