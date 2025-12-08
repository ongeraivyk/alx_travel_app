# listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with sample listings data."

    def handle(self, *args, **kwargs):
        # Create a default host if none exists
        host, created = User.objects.get_or_create(
            username="samplehost",
            defaults={"email": "host@example.com", "password": "password123"}
        )

        sample_listings = [
            {
                "title": "Beachfront Apartment",
                "description": "Beautiful 2-bedroom apartment facing the ocean.",
                "location": "Miami, FL",
                "price_per_night": 150.00,
                "host": host
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin perfect for a winter getaway.",
                "location": "Aspen, CO",
                "price_per_night": 200.00,
                "host": host
            },
            {
                "title": "City Loft",
                "description": "Modern loft in the heart of downtown.",
                "location": "New York, NY",
                "price_per_night": 250.00,
                "host": host
            }
        ]

        for listing_data in sample_listings:
            Listing.objects.get_or_create(
                title=listing_data["title"], defaults=listing_data
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
