# Generated by Django 4.0 on 2021-12-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0012_remove_my_status_user_my_status_institute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='createdon',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='updatedon',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='field_report',
            name='createdon',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='field_report',
            name='updatedon',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
