# Generated by Django 2.2.3 on 2019-07-29 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cycl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='parcours',
            options={'verbose_name_plural': 'Parcours'},
        ),
    ]