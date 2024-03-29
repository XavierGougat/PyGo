# Generated by Django 2.2.3 on 2019-08-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cycl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineup',
            options={'ordering': ['rider']},
        ),
        migrations.AlterModelOptions(
            name='manage',
            options={'ordering': ['staff']},
        ),
        migrations.AlterModelOptions(
            name='rider',
            options={'ordering': ['lastName', 'firstName']},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['lastName', 'firstName']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='country',
            name='code',
        ),
        migrations.AddField(
            model_name='country',
            name='alpha2Code',
            field=models.CharField(default='AB', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='alpha3Code',
            field=models.CharField(default='ABC', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='numericCode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
