# Generated by Django 4.0 on 2021-12-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0015_alter_field_report_poc_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factories',
            name='region',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='mrrname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report_poc',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='headoffice',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='institute',
            name='poc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]