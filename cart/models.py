from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.urls import reverse
from seller.models import Seller
from PIL import Image
# Create your models here.

class Category(models.Model):
    Category_Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Category_Name

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    Product_Name=models.CharField(max_length=50)
    Product_Description=models.CharField(max_length=150)
    Product_Starting_Price=models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    Product_Image_1 = models.ImageField(default="product_image1.jpg",upload_to='product_image')
    Product_Image_2 = models.ImageField(default="product_image2.jpg",upload_to='product_image')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image1 = Image.open(self.Product_Image_1.path)
        image2 = Image.open(self.Product_Image_2.path)
        if image1.height > 400 or image1.width > 400:
            output_size = (400, 400)
            image1.thumbnail(output_size)
        if image2.height > 400 or image2.width > 400:
            output_size = (400, 400)
            image2.thumbnail(output_size)
        image1.save(self.Product_Image_1.path,quality=60,optimize=True)
        image2.save(self.Product_Image_2.path,quality=60,optimize=True)

    def __str__(self):
        return self.Product_Name

    def get_absolute_url(self):
        return reverse('edit-profile')

class Order(models.Model):
    Order_Unique_Id =models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    Buyer_Name = models.CharField(max_length=20)
    Buyer_Phone_Number = PhoneNumberField(null = False, blank = False)
    Buyer_Email = models.EmailField(max_length=254)
    Buyer_pincode = models.CharField(max_length=6)
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    Order_Personalisation_Description = models.CharField(max_length=254)
    Message = models.CharField(max_length=50)
    Communication = models.BooleanField(default=True) #0->Both 1->Whatsapp Only 2->Email Only
    Order_Confirmation= models.BooleanField(default=False)
    Order_fulfilled=models.BooleanField(default=False)

    def __str__(self):
        String=f'{self.Order_Unique_Id} - Order for {self.Buyer_Name}'
        return String

    @property
    def get_order_id(self):
        return self.Order_Unique_Id

    def get_absolute_url(self):
        return reverse('Order-Details',kwargs={'pk':self.pk})

class OrderItem(models.Model):
    Order = models.ForeignKey(Order,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)

class Reviews(models.Model):
    Order=models.ForeignKey(Order,on_delete=models.CASCADE)
    Seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    Stars=models.DecimalField(max_digits=2, decimal_places=1)
    Review_Description=models.CharField(max_length=254)
