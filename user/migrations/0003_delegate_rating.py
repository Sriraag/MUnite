# Generated by Django 3.1 on 2020-08-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200826_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]