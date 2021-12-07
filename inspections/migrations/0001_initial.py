# Generated by Django 3.2.7 on 2021-12-07 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Action_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compliance_status', models.IntegerField()),
                ('showcausenoticestatus', models.BooleanField()),
                ('date', models.DateField()),
                ('finalrecommendation', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.action')),
            ],
        ),
        migrations.CreateModel(
            name='Basin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Factories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unitcode', models.IntegerField()),
                ('region', models.CharField(max_length=30)),
                ('basin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.basin')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.district')),
            ],
        ),
        migrations.CreateModel(
            name='Field_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uos', models.CharField(max_length=20)),
                ('uosdetail', models.CharField(max_length=20)),
                ('etpos', models.CharField(max_length=20)),
                ('etposdetail', models.CharField(max_length=20)),
                ('cpc', models.CharField(max_length=20)),
                ('ipc', models.CharField(max_length=20)),
                ('ppopd', models.CharField(max_length=20)),
                ('fwwpdbofm', models.CharField(max_length=20)),
                ('ocs', models.CharField(max_length=20)),
                ('sonfc', models.CharField(max_length=20)),
                ('mrr', models.CharField(max_length=20)),
                ('mrrname', models.CharField(max_length=40)),
                ('csac', models.CharField(max_length=20)),
                ('wc', models.CharField(max_length=20)),
                ('hc', models.CharField(max_length=20)),
                ('cc', models.CharField(max_length=20)),
                ('sfwc', models.CharField(max_length=20)),
                ('sfwcdetail', models.CharField(max_length=40)),
                ('fib', models.CharField(max_length=20)),
                ('fibdetail', models.CharField(max_length=20)),
                ('fietpinlet', models.CharField(max_length=20)),
                ('fietpinletdetail', models.CharField(max_length=20)),
                ('fietpoutlent', models.CharField(max_length=20)),
                ('fietpoutlentdetail', models.CharField(max_length=20)),
                ('fmetpoutletcdf', models.CharField(max_length=20)),
                ('fmetpoutletpdf', models.CharField(max_length=20)),
                ('os', models.CharField(max_length=20)),
                ('osdetail', models.CharField(max_length=20)),
                ('semfetp', models.CharField(max_length=20)),
                ('semfer', models.CharField(max_length=20)),
                ('specificobservations', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SPCB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100)),
                ('poc', models.CharField(max_length=40)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection_report_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZLDnorms', models.CharField(max_length=20)),
                ('bod', models.CharField(max_length=20)),
                ('bodLoad', models.CharField(max_length=20)),
                ('cod', models.CharField(max_length=20)),
                ('codLoad', models.CharField(max_length=20)),
                ('complianceStatus', models.IntegerField()),
                ('defunctETP', models.BooleanField()),
                ('dilutionInETP', models.BooleanField()),
                ('dissentBypassArrangement', models.BooleanField()),
                ('dissentWaterDischarge', models.BooleanField()),
                ('effluent', models.BooleanField()),
                ('finalRecommendation', models.CharField(max_length=20)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Inspection_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.inspection')),
            ],
        ),
        migrations.AddField(
            model_name='inspection',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.institute'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.factories'),
        ),
        migrations.CreateModel(
            name='Headoffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Field_report_poc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('field_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.field_report')),
            ],
        ),
        migrations.CreateModel(
            name='Field_report_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('field_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.field_report')),
            ],
        ),
        migrations.AddField(
            model_name='field_report',
            name='inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.inspection'),
        ),
        migrations.AddField(
            model_name='factories',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.sector'),
        ),
        migrations.AddField(
            model_name='factories',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.state'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.state'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Action_report_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('action_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.action_report')),
            ],
        ),
        migrations.AddField(
            model_name='action_report',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.spcb'),
        ),
        migrations.AddField(
            model_name='action',
            name='inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.inspection'),
        ),
    ]
