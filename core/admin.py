# coding: utf-8

from django.contrib import admin
from .models import Game, Competition, Rounds, Team, CompetitionHasTeam


class GameAdmin(admin.ModelAdmin):
    list_display = ('rounds', 'team_home', 'team_visitor', 'result_home',
                    'result_visitor', 'date', 'local')
    fieldsets = ((None, {
        'fields': (('team_home', 'team_visitor', 'rounds'),
                   ('date', 'local'),
                   ('result_home', 'result_visitor')),
    }),)


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {
        'fields': ('name', 'logo', 'creator_user'),
    }),)


class RoundsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'competition')
    fieldsets = ((None, {
        'fields': ('number', 'competition'),
    }),)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {
        'fields': ('name', 'flag'),
    }),)


class CompetitionHasTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'competition', 'team')
    fieldsets = ((None, {
        'fields': ('competition', 'team'),
    }),)


admin.site.register(Game, GameAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Rounds, RoundsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(CompetitionHasTeam, CompetitionHasTeamAdmin)
