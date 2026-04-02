from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=255)
    variety = models.CharField(max_length=255, blank=True, default="")
    field_name = models.CharField(max_length=255, blank=True, default="")
    area_acres = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    planted_date = models.DateField(null=True, blank=True)
    expected_harvest = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("planted", "Planted"), ("growing", "Growing"), ("ready", "Ready"), ("harvested", "Harvested"), ("failed", "Failed")], default="planted")
    estimated_yield = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class FarmField(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, default="")
    area_acres = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    soil_type = models.CharField(max_length=50, choices=[("clay", "Clay"), ("sandy", "Sandy"), ("loam", "Loam"), ("silt", "Silt")], default="clay")
    irrigation = models.CharField(max_length=50, choices=[("drip", "Drip"), ("sprinkler", "Sprinkler"), ("flood", "Flood"), ("rainfed", "Rainfed")], default="drip")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("fallow", "Fallow"), ("preparing", "Preparing")], default="active")
    current_crop = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Harvest(models.Model):
    crop_name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255, blank=True, default="")
    quantity_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quality_grade = models.CharField(max_length=50, choices=[("a", "A"), ("b", "B"), ("c", "C"), ("rejected", "Rejected")], default="a")
    harvest_date = models.DateField(null=True, blank=True)
    sold_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    buyer = models.CharField(max_length=255, blank=True, default="")
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.crop_name
