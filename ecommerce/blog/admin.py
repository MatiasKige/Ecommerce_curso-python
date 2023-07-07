from django.contrib import admin
from blog.models import Articles

# Register your models here.

@admin.register(Articles)
class Articles_admin(admin.ModelAdmin):
    list_display=["title","description","creation_date","author"]