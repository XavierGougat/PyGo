import sys
import os
import csv
from myapp.models import School, Lawyer

csv_filepathname =
"C:\Users\xgougat\Documents\GitHub\PyGoV2\PyGo\Django\Cycl\data.csv"

your_djangoproject_home =
"C:\Users\xgougat\Documents\GitHub\PyGoV2\PyGo\Django"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Cycl.settings'

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

old_school = None
for row in dataReader:
    if old_school != row[4]:
        old_school = row[4]
        school = School()
        school.name = old_school
        school.save()

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    lawyer = Lawyer()
    lawyer.firm_url = row[0]
    lawyer.firm_name = row[1]
    lawyer.first = row[2]
    lawyer.last = row[3]

    lawyer_school = School.objects.get(name=row[4])
    lawyer.school = lawyer_school

    lawyer.year_graduated = row[5]
    lawyer.save()
