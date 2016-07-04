# coding: utf-8
from django.contrib import admin

from .competition import CompetitionAdmin
from .game import GameAdmin
from .team import TeamAdmin
from .rounds import RoundsAdmin
from .competition_has_team import CompetitionHasTeamAdmin

from ..models import Game, Competition, Rounds, Team, CompetitionHasTeam


admin.site.register(Game, GameAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Rounds, RoundsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(CompetitionHasTeam, CompetitionHasTeamAdmin)
