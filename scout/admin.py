from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Team
from .models import Info

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Team)
admin.site.register(Info)


