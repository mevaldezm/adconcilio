# Generated by Django 2.0.4 on 2018-05-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_auto_20180510_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciclo',
            name='estado',
            field=models.CharField(blank=True, choices=[('a', 'activo'), ('i', 'inactivo')], default='a', max_length=1),
        ),
    ]
