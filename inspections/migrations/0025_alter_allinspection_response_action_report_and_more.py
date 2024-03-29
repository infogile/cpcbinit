# Generated by Django 4.0 on 2022-01-05 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0024_alter_action_report_files_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allinspection_response',
            name='action_report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspections.action_report'),
        ),
        migrations.AlterField(
            model_name='allinspection_response',
            name='attendance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspections.attendance'),
        ),
        migrations.AlterField(
            model_name='allinspection_response',
            name='inspection_report_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspections.inspection_report_data'),
        ),
    ]
