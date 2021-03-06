# Generated by Django 3.2.6 on 2021-09-16 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortlisted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_round_select_applicant', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sselect_job', to='recruiters.job')),
            ],
        ),
        migrations.CreateModel(
            name='second_Selected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_round_select_applicant', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SSselect_job', to='recruiters.job')),
            ],
        ),
        migrations.CreateModel(
            name='first_Selected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_round_select_applicant', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fselect_job', to='recruiters.job')),
            ],
        ),
    ]
