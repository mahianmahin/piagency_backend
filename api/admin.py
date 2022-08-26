from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'github_url']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation']
