# Generated by Django 2.2.3 on 2019-07-30 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cycl', '0012_auto_20190730_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lastLogin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='team',
            name='abreviation',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='bike',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
