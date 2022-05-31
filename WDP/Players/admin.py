from django.contrib import admin

from .models import Player
 
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("nickname", "real_name","real_surname","nationality","team","region","next_match_date","next_match_url",)
 
admin.site.register(Player, PlayerAdmin)
