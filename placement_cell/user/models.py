from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Custmuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    dob = models.DateField(auto_now=True)
    phone_reg = RegexValidator(regex=r"(\+\d{1,3})?,?\s?\d{8,13}", message="Enter valid phone number")
    phone_num = models.CharField(validators=[phone_reg], blank=True,null=True,max_length=16,unique=True)
    gender_choice= ( 
    ("male", "male"), 
    ("female", "female"), 
    )
    gender = models.CharField(max_length=18,choices=gender_choice,null=True,blank=True)


    def __str__(self):
        return self.user
        


