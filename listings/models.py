from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(
        max_length= 15,
        validators=[MinLengthValidator(5)]
    )
    description = models.TextField(blank=True) # Optional field, keeping it blank wont give error
    price = models.IntegerField()
    bedrooms = models.IntegerField() 
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1) # must be smaller than 100 and only have 1 decimal place. here max_digits = 3 counts the digit after decimal as well
    garage = models.IntegerField(default=0, null=True,  blank=True)
    sqr_ft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=6, decimal_places=1)
    img_main = models.ImageField(upload_to='photos/homes/%Y/%m/%d/')
    img_1 = models.ImageField(upload_to='photos/homes/%Y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='photos/homes/%Y/%m/%d/', blank=True)
    img_3 = models.ImageField(upload_to='photos/homes/%Y/%m/%d/', blank=True)
    img_4 = models.ImageField(upload_to='photos/homes/%Y/%m/%d/', blank=True)
    img_5 = models.ImageField(upload_to='photos/homes/%Y/%m/%d/', blank=True)
    img_6 = models.ImageField(upload_to='photos/homes/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    # list_date = models.DateField(auto_now_add=True) #auto_now_add will add the date when the object is created but it makes the field immutable
    list_date_created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title   # to display the listings via title in the admin panel