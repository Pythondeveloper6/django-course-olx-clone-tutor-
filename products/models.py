from django.db import models
from django.contrib.auth.models import User
# Create your models here.

AD_TYPE = (
    ('Sell' , 'Sell'),
    ('Exchange' , 'Exchange'),
)

PRODUCT_CONDITION = (
    ('New' , 'New'),
    ('Excellent Condition' , 'Excellent Condition'),
    ('Good Condition' , 'Good Condition'),
    ('Bad Condition' , 'Bad Condition'),
)

PAY_TYPE = (
    ('Cash' , 'Cash'),
    ('Visa' , 'Visa'),
)

class Product(models.Model):
    owner = models.ForeignKey(User, related_name='product_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand', related_name='product_brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='product_category', on_delete=models.CASCADE)
    ad_type = models.CharField(max_length=10 , choices=AD_TYPE)
    condition = models.CharField(max_length=20 , choices=PRODUCT_CONDITION)
    pay = models.CharField(max_length=10 , choices= PAY_TYPE)
    image = models.ImageField(upload_to='product/')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='brand/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

