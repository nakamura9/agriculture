# Generated by Django 2.2 on 2019-10-15 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191014_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
