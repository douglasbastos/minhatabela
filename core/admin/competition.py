# coding: utf-8
from django.contrib import admin


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {
        'fields': ('name', 'logo', 'creator_user'),
    }),)
