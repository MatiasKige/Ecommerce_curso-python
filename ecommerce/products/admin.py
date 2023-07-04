from django.contrib import admin
from products.models import Products

# Register your models here.

# admin.site.register(Products)

#       Otra manera de registrar un modelo:

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display=["name","price","stock","is_active"]