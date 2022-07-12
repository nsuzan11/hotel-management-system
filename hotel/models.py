from tabnanny import verbose
from unittest.util import _MIN_END_LEN
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime 
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Hotel(models.Model):
    class Meta:
        verbose_name_plural = 'Hotel'
    hotel_name = models.CharField(max_length=15)
    opening_hour = models.CharField(max_length=15)
    closing_hour = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    footer_text = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.hotel_name

@receiver(pre_delete, sender=Hotel)
def my_callback(sender, **kwargs):
    raise ValidationError("cannot delete")
    

    
class Bill(models.Model):
    class Meta:
        verbose_name_plural = 'Bill'
    room_price = models.ForeignKey('hotel.Room',on_delete = models.PROTECT)
    user_name = models.ForeignKey(User,on_delete = models.PROTECT)
    
    def __str__(self) -> str:
        return self.pk.__str__()


class Menu(models.Model):
    class Meta:
        verbose_name_plural = 'Menu'
    food_menu = models.CharField(max_length=30)
    bar_menu = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    room_type = models.CharField(max_length=30,null=False,blank=False,unique=True)
    room_price = models.PositiveIntegerField(blank=False,null=False)
    quantity = models.PositiveSmallIntegerField(blank=False,null=False)
    description = models.TextField()

    def __str__(self) -> str:
        return self.room_type


class Booking(models.Model):
    room_type = models.ForeignKey(Room,on_delete = models.PROTECT)
    user_info = models.ForeignKey(User,on_delete = models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    start_day = models.DateField(verbose_name="start date AD")
    end_day = models.DateField(verbose_name="end date AD")
    no_people = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, validators=[MinValueValidator(10)], null=True) 
    
    def __str__(self) -> str:
        return self.room_type.room_type 

    def clean(self):
        start = self.start_day
        end = self.end_day
        if start > end:
            raise ValidationError("Start date crosses end date")
        if start < datetime.date.today():
            raise ValidationError("Start date is in the past")
        if end < datetime.date.today():
            raise ValidationError("End date is in the past")

# class TotalBooking:
#     all_booking = 
