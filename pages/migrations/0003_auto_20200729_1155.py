# Generated by Django 3.0.4 on 2020-07-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200729_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpreneur',
            name='firstName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='enterpreneur',
            name='ico',
            field=models.CharField(max_length=8),
        ),
    ]