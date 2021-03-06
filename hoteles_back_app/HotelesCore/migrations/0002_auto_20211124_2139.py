# Generated by Django 3.2.9 on 2021-11-25 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelesCore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='begin_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 444906)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 444906)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 444906)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 443906)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 443906)),
        ),
        migrations.AlterField(
            model_name='room',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 443906)),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 39, 1, 443906)),
        ),
    ]
