# Generated by Django 4.0 on 2021-12-23 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0025_alter_action_report_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action_report',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.user'),
        ),
    ]
