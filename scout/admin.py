from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Team, TeamMatch
from .models import Info
from .models import Match
admin.site.register(Team)
admin.site.register(Info)
admin.site.register(Match)
admin.site.register(TeamMatch)

