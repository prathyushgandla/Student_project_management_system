# Generated by Django 3.2 on 2021-12-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeproject', '0002_auto_20211204_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='academic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
