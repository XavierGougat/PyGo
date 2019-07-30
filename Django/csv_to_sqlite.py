import csv
from Cycl import models

f = open('lequipe_etape.csv', 'r')

for line in f:
    line = line.split(';')
    team = models.Team()
    team.name = line[0]
    team.save()

f.close()
