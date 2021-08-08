from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField


class Seller(models.Model):
    Owner = models.OneToOneField(User, on_delete=models.CASCADE)
    StoreName = models.CharField(max_length=20)
    StoreLogo = models.ImageField(default="logo.jpg",upload_to='profile_logo')
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    pincode = models.CharField(max_length=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank = False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank = False)
    Deliver_anywhere=models.BooleanField(default=False)
    Local_Delivery_Distance=models.IntegerField(default=0)
    insta_social = models.CharField(max_length=10)
    ContactPreference = models.IntegerField(default=0) #0->Both 1->Whatsapp Only 2->Email Only
    Premium=models.BooleanField(default=False)
    Premium_start_date=models.DateTimeField( null = True, blank = False)
    Premium_end_date=models.DateTimeField( null = True, blank = False)
    Account_created_on=models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return self.StoreName

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.StoreLogo.path)
        if image.height > 200 or image.width > 200:
            output_size = (200, 200)
            image.thumbnail(output_size)
        image.save(self.StoreLogo.path,quality=20,optimize=True)


class SellerInavailability(models.Model):
    seller=models.ForeignKey(Seller, on_delete=models.CASCADE)
    date_unavailable = models.DateTimeField()

