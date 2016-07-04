# coding: utf-8
from django.db import models
from .competition import Competition
from .team import Team


class CompetitionHasTeam(models.Model):
    competition = models.ForeignKey(Competition)
    team = models.ForeignKey(Team)

    class Meta:
        verbose_name = 'Time/competição'
        verbose_name_plural = 'Times/competições'
