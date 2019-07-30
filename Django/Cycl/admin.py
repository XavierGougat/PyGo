from django.contrib import admin
from .models import (Race, Stage, Serie, Parcours, Team, Rider, Lineup,
                     Country, Result, Register, StartList, Player, Roster,
                     Ranking)

admin.site.register(Race)
admin.site.register(Stage)
admin.site.register(Serie)
admin.site.register(Parcours)
admin.site.register(Team)
admin.site.register(Rider)
admin.site.register(Lineup)
admin.site.register(Country)
admin.site.register(Result)
admin.site.register(Register)
admin.site.register(StartList)
admin.site.register(Player)
admin.site.register(Roster)
admin.site.register(Ranking)
