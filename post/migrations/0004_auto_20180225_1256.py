# Generated by Django 2.0.2 on 2018-02-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20180225_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=8, unique=True),
        ),
    ]
