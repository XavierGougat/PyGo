from django.db import models
from django.utils import datetime


def current_year():
    return datetime.date.today().year


class Race(models.Model):
    name = models.CharField(max_length=100)
    session = models.IntegerField(null=True)
    startDate = models.DateTimeField(null=False,
                                     verbose_name="When the race starts")
    finishDate = models.DateTimeField(null=False,
                                      verbose_name="When the race ends")
    series = models.ForeignKey('Serie',
                               default=1,
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.name.' - '.self.start_date.year()


class Stage(models.Model):
    name = models.Charfield(max_length=150)
    kilometers = models.FloatField(default=0)
    start = CharField(max_length=100)
    finish = CharField(max_length=100)
    date = models.DateTimeField(null=False)
    race = models.ForeignKey('Race',
                             default=1,
                             on_delete=models.CASCADE)
    parcours = models.ForeignKey('Parcours',
                                 default=1,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.start + ' > ' + self.finish + ' (' + self.kilometers + 'k)'


class Serie(models.Model):
    name = models.CharField(max_length=50)
    text = models.Charfield(max_length=150)


class Parcours(models.Model):
    name = models.CharField(max_length=100)


class Team(models.Model):
    name = models.CharField(max_length=100)
    abreviation = models.CharField(max_length=3)
    bike = models.CharField(max_length=30)


class Rider():
    firstName = models.Charfield(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateTimeField(null=False)
    birthPlace = models.CharField(max_length=100)
    country = models.ForeignKey('Country',
                                default=1,
                                on_delete=models.CASCADE)
    weigth = models.FloatField(null=True)
    height = models.FloatField(null=True)
    uciRank = models.IntegerField(null=True)
    pcsRank = models.IntegerField(null=True)
    country = models.ManyToManyField(Team,
                                     related_name="riders")
