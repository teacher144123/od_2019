# Generated by Django 2.1.2 on 2019-05-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_house_stat_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='raw_stat',
            field=models.CharField(default='', max_length=200),
        ),
    ]