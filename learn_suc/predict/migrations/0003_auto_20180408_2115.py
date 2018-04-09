# Generated by Django 2.0.3 on 2018-04-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_auto_20180331_1553'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['name'], name='item_name_idx'),
        ),
        migrations.AddIndex(
            model_name='type',
            index=models.Index(fields=['name'], name='type_name_idx'),
        ),
    ]