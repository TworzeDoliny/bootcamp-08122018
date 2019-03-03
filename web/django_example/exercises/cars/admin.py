from django.contrib import admin

# Register your models here.
from cars.models import Car, Engine

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "production_year"]
    search_fields = ["brand"]
    list_filter = ["brand", "model", "body_type"]
# admin.site.register(Car, CarAdmin)

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ["type", "power"]
