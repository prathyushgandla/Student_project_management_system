# Generated by Django 3.2 on 2022-01-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeproject', '0007_auto_20220102_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='StudentMobileNumber4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='StudentMobileNumber5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
