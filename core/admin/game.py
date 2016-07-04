# coding: utf-8
from django.contrib import admin


class GameAdmin(admin.ModelAdmin):
    list_display = ('rounds', 'team_home', 'team_visitor', 'result_home',
                    'result_visitor', 'date', 'local')
    fieldsets = ((None, {
        'fields': (('team_home', 'team_visitor', 'rounds'),
                   ('date', 'local'),
                   ('result_home', 'result_visitor')),
    }),)
