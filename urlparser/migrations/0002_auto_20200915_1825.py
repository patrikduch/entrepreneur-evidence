# Generated by Django 3.0.8 on 2020-09-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='siteName',
            field=models.CharField(max_length=85),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=85),
        ),
    ]
