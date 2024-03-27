from django.db import models

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)


    def __str__(self):
        return self.catagory_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)


    def __str__(self):
        return self.product_name


class Customer(models.Model):
    ful_name = models.CharField(max_length=80)
    countri = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.ful_name


class Order(models.Model):
    order_name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)


    def __str__(self):
        return self.order_name


class Orderitem(models.Model):
    recipient_name = models.CharField(max_length=100)
    where_to_go = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.recipient_name


class ShippingAddress(models.Model):
    contri = models.CharField(max_length=80)
    citi = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.contri

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

