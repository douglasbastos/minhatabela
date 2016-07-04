# coding: utf-8
from django.db import models


class Team(models.Model):
    name = models.CharField('Nome', max_length=255)
    flag = models.ImageField('Escudo')

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __unicode__(self):
        return self.name
