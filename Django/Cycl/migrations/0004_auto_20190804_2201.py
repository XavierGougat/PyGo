# Generated by Django 2.2.3 on 2019-08-04 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cycl', '0003_auto_20190804_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('alpha3Code',), 'verbose_name_plural': 'Countries'},
        ),
    ]
