# Generated by Django 4.2.5 on 2023-09-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
