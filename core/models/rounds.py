# coding: utf-8
from django.db import models
from .competition import Competition


class Rounds(models.Model):
    number = models.PositiveSmallIntegerField()
    competition = models.ForeignKey(Competition)

    class Meta:
        verbose_name = 'Rodada'
        verbose_name_plural = 'Rodadas'

    def __unicode__(self):
        return '{} #{}'.format(self.competition.name, self.number)
