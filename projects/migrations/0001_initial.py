# Generated by Django 2.2 on 2019-10-14 21:13

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
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('estimated_cost', models.DecimalField(decimal_places=2, max_digits=16)),
                ('actual_cost', models.DecimalField(decimal_places=2, max_digits=16)),
                ('start_date', models.DateField()),
                ('completed_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InputCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MileStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=64)),
                ('actual', models.CharField(max_length=64)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'In Progress'), (1, 'Achieved'), (1, 'Failed')])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('symbol', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Fixed Term'), (2, 'Continuous')])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=16)),
                ('quantity', models.FloatField(default=1.0)),
                ('date', models.DateField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Activity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.InputCategory')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.UnitOfMeasure')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Role')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='activity',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Agent'),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('estimated_cost', models.DecimalField(decimal_places=2, max_digits=16)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Activity')),
                ('taken_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Agent')),
            ],
        ),
    ]
