from django.contrib import admin

from .models import Training


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_date', 'location')
    list_filter = ('training_date',)
    date_hierarchy = 'training_date'
    ordering = ('training_date',)
    search_fields = ('location',)
