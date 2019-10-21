from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Team
from .models import Info
from .models import SkystoneMatch
admin.site.register(Team)
admin.site.register(Info)
admin.site.register(SkystoneMatch)
