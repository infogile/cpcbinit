# Generated by Django 4.0 on 2021-12-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0014_alter_factories_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_report_poc',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report_poc',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
