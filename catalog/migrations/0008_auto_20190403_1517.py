# Generated by Django 2.1.7 on 2019-04-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20190403_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='id',
            field=models.IntegerField(default='0', primary_key=True, serialize=False),
        ),
    ]
