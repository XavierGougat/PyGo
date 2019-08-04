import csv
import datetime
from Cycl import models

f = open('Cycl/scrap/csv/Countries_codes_ISO_3166-1.csv', 'r')

for line in f:
    line = line.split(',')

    country = models.Country()
    country.name = line[0]
    country.alpha2Code = line[1]
    country.alpha3Code = line[2]
    country.numericCode = int(line[3])
    country.save()

f.close()
