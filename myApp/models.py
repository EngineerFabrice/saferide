from django.db import models

#from django.db import models

# User Model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)  # example: admin, driver, car owner
    password = models.CharField(max_length=255)
    can_register = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Admin Model
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"Admin: {self.user.name}"

# Location Model
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Location {self.location_id}"

# Driver Model
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    car_owner_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name

# Booking Model
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup_location = models.ForeignKey(Location, related_name="pickup_location", on_delete=models.SET_NULL, null=True)
    drop_location = models.ForeignKey(Location, related_name="drop_location", on_delete=models.SET_NULL, null=True)
    booking_date = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"Booking ID: {self.booking_id}"

# Feedback Model
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"Feedback {self.feedback_id}"

