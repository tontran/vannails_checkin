# Generated by Django 3.1.3 on 2020-11-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_api', '0005_remove_staff_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
