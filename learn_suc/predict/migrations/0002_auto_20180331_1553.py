# Generated by Django 2.0.3 on 2018-03-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedding',
            name='embedding',
            field=models.TextField(),
        ),
    ]
