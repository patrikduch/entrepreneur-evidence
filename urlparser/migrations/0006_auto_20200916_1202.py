# Generated by Django 3.0.8 on 2020-09-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlparser', '0005_auto_20200916_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='siteName',
            field=models.CharField(max_length=85, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=85, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
