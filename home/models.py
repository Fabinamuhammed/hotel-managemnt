from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
# from selection.models import User

# Create your models here.


# class login(models.Model):
#     name =models.CharField(max_length=100)
#     email = models.EmailField(
#         verbose_name='e-mail',
#         null=True
#     )
#     password=models.CharField(max_length=100)
#     address=models.CharField(max_length=100)
#     phno = models.CharField(
#         validators=[MinLengthValidator(5)],
#         max_length=12,
#         null=True,
#     )

# def __str__(self):
#     return str(self.email+""+self.password)
class User(models.Model):
   Userid = models.CharField(max_length=50, primary_key=True)
   name = models.CharField(max_length=100)
   password=models.CharField(max_length=100)
   email = models.EmailField(max_length=50)
   address=models.CharField(max_length=100, blank= True)
   cell_phone = models.CharField(max_length=200, blank=True)

class Hotel(models.Model):
   H_id = models.CharField(max_length=50, primary_key=True)
   H_name = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   district = models.CharField(max_length=100)
   pincode = models.CharField(max_length=100)
   category = models.CharField(max_length=100)

class rooms(models.Model):
   room_id = models.CharField(max_length=50,unique=True)
   H = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel')
   room_no = models.IntegerField()
   room_type = models.CharField(max_length=100)
   price = models.IntegerField()

class Booking(models.Model):
   B_id = models.CharField(max_length=50,unique=True)
   H = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hoteli')
   room_id = models.ForeignKey(rooms, on_delete=models.CASCADE, related_name='rooms')
   Userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='useri')
   room_no = models.ForeignKey(rooms, on_delete=models.CASCADE, related_name='roomn')