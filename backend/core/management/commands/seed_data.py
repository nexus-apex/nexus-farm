from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Crop, FarmField, Harvest
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusFarm with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusfarm.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Crop.objects.count() == 0:
            for i in range(10):
                Crop.objects.create(
                    name=f"Sample Crop {i+1}",
                    variety=f"Sample {i+1}",
                    field_name=f"Sample Crop {i+1}",
                    area_acres=round(random.uniform(1000, 50000), 2),
                    planted_date=date.today() - timedelta(days=random.randint(0, 90)),
                    expected_harvest=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["planted", "growing", "ready", "harvested", "failed"]),
                    estimated_yield=round(random.uniform(1000, 50000), 2),
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Crop records created'))

        if FarmField.objects.count() == 0:
            for i in range(10):
                FarmField.objects.create(
                    name=f"Sample FarmField {i+1}",
                    location=f"Sample {i+1}",
                    area_acres=round(random.uniform(1000, 50000), 2),
                    soil_type=random.choice(["clay", "sandy", "loam", "silt"]),
                    irrigation=random.choice(["drip", "sprinkler", "flood", "rainfed"]),
                    status=random.choice(["active", "fallow", "preparing"]),
                    current_crop=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 FarmField records created'))

        if Harvest.objects.count() == 0:
            for i in range(10):
                Harvest.objects.create(
                    crop_name=f"Sample Harvest {i+1}",
                    field_name=f"Sample Harvest {i+1}",
                    quantity_kg=round(random.uniform(1000, 50000), 2),
                    quality_grade=random.choice(["a", "b", "c", "rejected"]),
                    harvest_date=date.today() - timedelta(days=random.randint(0, 90)),
                    sold_price=round(random.uniform(1000, 50000), 2),
                    buyer=f"Sample {i+1}",
                    revenue=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 Harvest records created'))
