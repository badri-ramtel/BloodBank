from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blood_Bank(models.Model):
    bank_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    contact_person_name = models.CharField(max_length=50)
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

