from django.db import models


# Create your models here.
class Contact(models.Model):
    contact_name=models.CharField(max_length=255)
    contact_email=models.EmailField(max_length=255)
    contact_msg=models.CharField(max_length=255)
   
    def __str__(self):
        return self.contact_name
    

class Registration(models.Model):
    reg_name=models.CharField(max_length=255)
    reg_email=models.EmailField(max_length=255)
    reg_mob=models.CharField(max_length=255)
    reg_username=models.CharField(max_length=255)
    reg_pwd=models.CharField(max_length=255)

    def __str__(self):
        return self.reg_name
    

class Product(models.Model):
    pro_name=models.CharField(max_length=255)
    pro_catid=models.IntegerField(null=True)
    pro_price=models.FloatField()
    pro_image=models.FileField(upload_to="products")
   
    def __str__(self):
        return self.pro_name
    
class Category(models.Model):
    cat_name=models.CharField(max_length=255)
    cat_image=models.FileField(upload_to="categories")
   
    def __str__(self):
        return self.cat_name
    
class Cart(models.Model):
    cart_user=models.CharField(max_length=255)
    cart_pid=models.IntegerField(null=True)
    cart_name=models.CharField(max_length=255)
    cart_price=models.FloatField(null=True)
    cart_image=models.FileField()
    cart_qty=models.IntegerField()
    cart_amount=models.FloatField()
   
    def __str__(self):
        return self.cart_name

class Order(models.Model):
    order_name=models.CharField(max_length=255)
    order_address=models.CharField(max_length=255)
    order_number=models.IntegerField()
    order_user=models.CharField(max_length=255,null=True)
    order_pid=models.IntegerField(null=True)
    order_proname=models.CharField(max_length=255,null=True)
    order_price=models.FloatField(null=True)
    order_image=models.FileField(null=True)
    order_qty=models.IntegerField(null=True)
    order_amount=models.FloatField(null=True)
    order_payment=models.CharField(max_length=255,null=True)
    
   
    def __str__(self):
         return self.order_name
    