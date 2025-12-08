# listings/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
    """
    Represents a property/listing that can be booked.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_listings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Represents a booking for a listing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-calculate total price
        num_nights = (self.end_date - self.start_date).days
        self.total_price = self.listing.price_per_night * num_nights
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.id} for {self.listing}"


class Review(models.Model):
    """
    Represents a review for a listing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer} - {self.rating}/5"
