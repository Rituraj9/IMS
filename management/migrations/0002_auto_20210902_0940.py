# Generated by Django 3.2.6 on 2021-09-02 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='applied_jobs',
        ),
        migrations.DeleteModel(
            name='job_pos',
        ),
        migrations.DeleteModel(
            name='stu_details',
        ),
    ]
