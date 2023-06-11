from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model): 
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price =models.DecimalField(max_digit=6,decimal_places=2)
    inventory =models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'), 
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')


class Order(models.Model):
    PAYMENT_PEMDING ='P'
    PAYMENT_COMPLETE ='C'
    PAYMENT_FAIL='F'
    
    PAYMENT_STATUS =[
        (PAYMENT_PEMDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAIL, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.IntegerField(max_length=1,choices=PAYMENT_STATUS, default=PAYMENT_PEMDING)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)




