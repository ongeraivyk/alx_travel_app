# ALX Travel App — Milestone 2

This project implements the backend logic for travel listings including:

## ✔ Database Models
- Listing  
- Booking  
- Review  

These models define relationships such as:
- Listing → Booking (One-to-Many)
- Listing → Review (One-to-Many)
- User → Hosting and Bookings

---

## ✔ Serializers
Located in `listings/serializers.py`
- ListingSerializer
- BookingSerializer

They convert model data into JSON for API responses using Django REST Framework.

---

## ✔ Seeder Command
A custom Django management command is included:

