# Generated by Django 2.0.4 on 2018-05-14 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0011_auto_20180510_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(default='event_images/None/no-img.jpg', upload_to='event_images/'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='duracion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 5, 14, 4, 0)),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='imagen',
            field=models.ImageField(default='promo_images/None/no-img.jpg', upload_to='promo_images/'),
        ),
    ]
