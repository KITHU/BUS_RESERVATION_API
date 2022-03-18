"""Module doc string ."""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Passager(models.Model):
    """Class doc string."""

    GENDERS = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )

    full_name = models.CharField(max_length=80, unique=False, blank=False)
    id_or_passport = models.PositiveIntegerField(blank=False, unique=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=255)
    nationality = models.CharField(max_length=15, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Methods doc string."""
        return self.full_name


class Bus(models.Model):
    """Class doc string."""

    no_of_seat = models.IntegerField(validators=[
        MinValueValidator(14), MaxValueValidator(67)])
    bus_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        """Methods doc string."""
        return self.bus_name + " " + str(self.no_of_seat) + " seater."


class Route(models.Model):
    """Class doc string."""

    from_destination = models.CharField(max_length=255, blank=False,
                                        null=False)
    to_destination = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        """Methods doc string."""
        return self.from_destination + " to " + self.to_destination


class Schedule(models.Model):
    """Class doc string."""

    departure_time = models.TimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    date_of_travel = models.DateField(auto_now=False, auto_now_add=False)
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)


class Reservation(models.Model):
    """Class doc string."""

    customer_name = models.CharField(max_length=80, unique=False, blank=False)
    seat_no = models.IntegerField()
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
