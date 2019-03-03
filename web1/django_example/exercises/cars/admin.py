from django.contrib import admin
from cars.models import Car, Engine
# Register your models here.

@admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "production_year"]
    search_fields = ["brand"]
    list_filter = ["brand", "model", "body_type"]

@admin.register(Engine)
class EndgineAdmin(admin.ModelAdmin):
    list_display = ["type", "power"]
