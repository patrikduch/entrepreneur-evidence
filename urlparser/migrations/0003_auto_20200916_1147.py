# Generated by Django 3.0.8 on 2020-09-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlparser', '0002_auto_20200915_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
