# Generated by Django 4.0 on 2021-12-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0006_factories_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factories',
            name='unitcode',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
