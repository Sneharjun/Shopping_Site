from django.contrib import admin
from . models import Contact
from . models import Registration
from . models import Product
from . models import Category
from . models import Cart
from . models import Order

# Register your models here.
admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
