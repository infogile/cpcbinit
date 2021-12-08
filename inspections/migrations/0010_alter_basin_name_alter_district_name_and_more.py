# Generated by Django 4.0 on 2021-12-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0009_alter_user_password_alter_user_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basin',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='cc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='cpc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='csac',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='etpos',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='etposdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fib',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fibdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fietpinlet',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fietpinletdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fietpoutlent',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fietpoutlentdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fmetpoutletcdf',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fmetpoutletpdf',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='fwwpdbofm',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='hc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='ipc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='mrr',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='ocs',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='os',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='osdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='ppopd',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='semfer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='semfetp',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='sfwc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='sfwcdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='sonfc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='specificobservations',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='uos',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='uosdetail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='field_report',
            name='wc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
