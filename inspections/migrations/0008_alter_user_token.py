# Generated by Django 4.0 on 2021-12-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0007_alter_factories_unitcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='None', max_length=50, unique=True),
        ),
    ]
