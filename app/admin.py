from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','name']

admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','selling_price','discount_price','description','brand','category','product_image']

admin.site.register(Product,ProductAdmin)

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','order_date','status']

admin.site.register(OrderPlaced,OrderPlacedAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

admin.site.register(Cart,CartAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=['user','name','hno','street','city','state','pincode']

admin.site.register(Address,AddressAdmin)