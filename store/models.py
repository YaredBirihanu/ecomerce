
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    old_cart = models.CharField(max_length=50, blank=True, null=True)

   
    def __str__(self):
        return self.user.username


    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()


    post_save.connect(create_profile, sender=User)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    #add sell stuff to product
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(decimal_places=2, max_digits=6,default=0)


    
    def __str__(self):
        return self.name

#customer_orders  
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # Add other fields as needed
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    address=models.TextField(max_length=10,default='')
    phone=models.CharField(max_length=10)
    date=models.DateField(default=datetime.datetime.today)
    
    
    def __str__(self):
        return self.product
        #return f'Order for {self.customer.first_name} {self.customer.last_name}'
