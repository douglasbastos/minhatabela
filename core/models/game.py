# coding: utf-8
from django.db import models
from .team import Team
from .rounds import Rounds


class Game(models.Model):
    name = models.CharField('Nome', max_length=255)
    team_home = models.ForeignKey(Team)
    team_visitor = models.ForeignKey(Team)
    result_home = models.PositiveSmallIntegerField()
    result_visitor = models.PositiveSmallIntegerField()
    rounds = models.ForeignKey(Rounds)
    local = models.CharField('Local', max_length=255)
    date = models.DateTimeField('Data e Hora')

    class Meta:
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'

    def __unicode__(self):
        return self.name
