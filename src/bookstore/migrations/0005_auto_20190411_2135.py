# Generated by Django 2.1.5 on 2019-04-11 21:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20190411_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date2',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
