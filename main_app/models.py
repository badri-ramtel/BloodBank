from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blood_Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    contact_person_name = models.CharField(max_length=50, null=True)
    map = models.CharField(max_length=10)
    email = models.EmailField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default='badri')

    def __str__(self):
        return f'{self.bank_name}'

    class Meta:
        verbose_name_plural = 'BloodBank'
        db_table = 'bloodbank'

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()


    def __str__(self):
        return f'{self.username}'
    
    # class Meta:
    #     verbose_name_plural = 'Users'
    #     bd_tabel = 'user'