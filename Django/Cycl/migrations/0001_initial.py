# Generated by Django 2.2.3 on 2019-07-29 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivalDate', models.DateTimeField(verbose_name='When the rider starts with the team')),
                ('leavingDate', models.DateTimeField(verbose_name='When the rider leaves the team')),
            ],
        ),
        migrations.CreateModel(
            name='Parcours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('session', models.IntegerField(null=True)),
                ('startDate', models.DateTimeField(verbose_name='When the race starts')),
                ('finishDate', models.DateTimeField(verbose_name='When the race ends')),
            ],
            options={
                'ordering': ['startDate'],
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abreviation', models.CharField(max_length=3)),
                ('bike', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('kilometers', models.FloatField(default=0)),
                ('start', models.CharField(max_length=100)),
                ('finish', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('parcours', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cycl.Parcours')),
                ('race', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cycl.Race')),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('birthDate', models.DateTimeField()),
                ('birthPlace', models.CharField(max_length=100)),
                ('weigth', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('uciRank', models.IntegerField(null=True)),
                ('pcsRank', models.IntegerField(null=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cycl.Country')),
                ('team', models.ManyToManyField(related_name='_rider_team_+', through='Cycl.Lineup', to='Cycl.Team')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cycl.Serie'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cycl.Rider'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cycl.Team'),
        ),
    ]