from django.contrib import admin
from .models import (Race, Stage, Serie, Parcours, Team, Rider, Lineup,
                     Country, Result, Register, StartList, Player, Roster,
                     Ranking, Teamcategory, Staff, Manage)


class RiderAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'nation', 'continent', 'uciid')
    search_fields = ['lastName', 'firstName', 'nation', 'continent', 'uciid']
    list_filter = ('lastName', 'firstName', 'nation', 'continent', 'uciid')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'alpha2Code', 'alpha3Code')
    search_fields = ['name', 'alpha2Code', 'alpha3Code']
    list_filter = ('name', 'alpha2Code', 'alpha3Code')


class LineupAdmin(admin.ModelAdmin):
    list_display = ('rider', 'team')
    search_fields = ['rider__lastName', 'rider__firstName', 'team__name']
    list_filter = ('rider__nation',)

admin.site.register(Race)
admin.site.register(Stage)
admin.site.register(Serie)
admin.site.register(Parcours)
admin.site.register(Team)
admin.site.register(Rider, RiderAdmin)
admin.site.register(Lineup, LineupAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Result)
admin.site.register(Register)
admin.site.register(StartList)
admin.site.register(Player)
admin.site.register(Roster)
admin.site.register(Ranking)
admin.site.register(Teamcategory)
admin.site.register(Staff)
admin.site.register(Manage)
