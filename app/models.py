from django.db import models
from django.contrib.auth.models import User,AbstractUser
User._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').null = False
STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('J&K','J&K'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh	','Uttar Pradesh	'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
)
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Shipped','Shipped'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancled','Cancled'),
)
CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.id)

class Product(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=255)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=50,default="Accepted")

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    hno = models.CharField(max_length=255)
    locality = models.CharField(max_length=255,default="NA")
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255,blank=False)
    state = models.CharField(max_length=255,choices=STATE_CHOICES,blank=False)
    pincode = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.id)