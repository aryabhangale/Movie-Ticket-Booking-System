# Generated by Django 4.0.3 on 2022-05-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0017_auto_20201016_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='pepsi',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seat',
            name='popcorn',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
