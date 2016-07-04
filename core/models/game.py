# coding: utf-8
from django.db import models
from .team import Team
from .rounds import Rounds


class Game(models.Model):
    name = models.CharField('Nome', max_length=255)
    team_home = models.ForeignKey(Team, related_name='Mandante')
    team_visitor = models.ForeignKey(Team, related_name='Visitante')
    result_home = models.PositiveSmallIntegerField('Resultado Mandante', blank=True, null=True)
    result_visitor = models.PositiveSmallIntegerField('Resultado Visitante', blank=True, null=True)
    rounds = models.ForeignKey(Rounds)
    local = models.CharField('Local', max_length=255, blank=True, null=True)
    date = models.DateTimeField('Data e Hora', blank=True, null=True)

    class Meta:
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'

    def __unicode__(self):
        return self.name
