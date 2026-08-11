from django.contrib import admin

from .models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'opponent', 'is_home', 'location', 'goals_for', 'goals_against')
    list_filter = ('is_home', 'match_date')
    date_hierarchy = 'match_date'
    ordering = ('match_date',)
    search_fields = ('opponent', 'location')

