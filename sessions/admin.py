from django.contrib import admin
from .models import Session

# Register your models here.
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "wave", "level", "starts_at")
    list_filter = ("wave", "level", "starts_at")
    ordering = ("-starts_at", "level_id", "title")