from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=255)

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
