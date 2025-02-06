from django.contrib import admin
from leaderboard.models import Player

# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
