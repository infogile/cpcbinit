# Generated by Django 4.0 on 2022-06-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0025_alter_allinspection_response_action_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection_report_data',
            name='finalRecommendation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
