# Generated by Django 3.1.4 on 2020-12-30 21:44

import datetime
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
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_profile', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=100)),
                ('platform_user_id', models.CharField(blank=True, max_length=150, null=True)),
                ('platform_username', models.CharField(max_length=100)),
                ('platform_public_id', models.CharField(max_length=100)),
                ('platform_candidate_bio', models.TextField(default='')),
                ('number_of_strengths', models.PositiveIntegerField()),
                ('number_of_awards', models.PositiveIntegerField()),
                ('number_of_interests', models.PositiveIntegerField()),
                ('number_of_jobs', models.PositiveIntegerField()),
                ('number_of_projects', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreed_terms_and_conditions', models.BooleanField(default=False)),
                ('terms_and_conditions_date', models.DateTimeField(default=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort_management.candidate')),
                ('organizations', models.ManyToManyField(to='cohort_management.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform_opportunity_id', models.CharField(max_length=100)),
                ('opportunity_objective', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cohort_management.organization')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort_management.manager')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort_management.platform')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort_management.candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort_management.cohort'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='interests',
            field=models.ManyToManyField(to='cohort_management.Interest'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort_management.platform'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='strengths',
            field=models.ManyToManyField(to='cohort_management.Strength'),
        ),
    ]
