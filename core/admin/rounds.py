# coding: utf-8
from django.contrib import admin


class RoundsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'competition')
    fieldsets = ((None, {
        'fields': ('number', 'competition'),
    }),)
