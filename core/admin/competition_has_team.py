# coding: utf-8
from django.contrib import admin


class CompetitionHasTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'competition', 'team')
    fieldsets = ((None, {
        'fields': ('competition', 'team'),
    }),)
