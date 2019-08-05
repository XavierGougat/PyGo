import csv
import datetime
from django.shortcuts import get_object_or_404
from Cycl import models

f = open('Cycl/scrap/csv/riders_WTT.csv', 'r')

for line in f:
    line = line.split(';')

    if line[0] == "Rider":
        rider = models.Rider()
        rider.lastName = line[1]
        rider.firstName = line[2]
        rider.birthDate = datetime.datetime.strptime(line[3], "%d/%m/%Y").date()
        try:
            nation = models.Country.objects.get(alpha3Code=line[6])
        except models.Country.DoesNotExist:
            nation = None
        rider.nation = nation
        team = models.Team()
        team = get_object_or_404(models.Team, abreviation=line[8])
        rider.save()
        rider.team.add(team)
        rider.uciid = line[10]
        rider.save()
    else:
        staff = models.Staff()
        staff.function = line[0]
        staff.lastName = line[1]
        staff.firstName = line[2]
        try:
            nation = models.Country.objects.get(alpha3Code=line[6])
        except models.Country.DoesNotExist:
            nation = None
        staff.nation = nation
        team = models.Team()
        team = get_object_or_404(models.Team, abreviation=line[8])
        staff.save()
        staff.team.add(team)
        staff.uciid = line[10]
        staff.save()

f.close()
