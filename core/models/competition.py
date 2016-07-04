# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from .team import Team


class Competition(models.Model):
    name = models.CharField('Nome', max_length=255)
    logo = models.ImageField('Logo')
    teams = models.ManyToManyField(Team, through='CompetitionHasTeam')
    creator_user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'

    def __unicode__(self):
        return self.name
