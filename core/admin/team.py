# coding: utf-8
from django.contrib import admin


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {
        'fields': ('name', 'flag'),
    }),)
