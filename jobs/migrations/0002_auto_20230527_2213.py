# Generated by Django 3.2 on 2023-05-27 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
    ]
