from django.contrib import admin
from .models import Crop, FarmField, Harvest

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ["name", "variety", "field_name", "area_acres", "planted_date", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "variety", "field_name"]

@admin.register(FarmField)
class FarmFieldAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "area_acres", "soil_type", "irrigation", "created_at"]
    list_filter = ["soil_type", "irrigation", "status"]
    search_fields = ["name", "location", "current_crop"]

@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ["crop_name", "field_name", "quantity_kg", "quality_grade", "harvest_date", "created_at"]
    list_filter = ["quality_grade"]
    search_fields = ["crop_name", "field_name", "buyer"]
