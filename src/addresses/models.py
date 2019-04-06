from django.db import models
from accounts.models import Profile

# Create your models here.
ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping','Shipping'),
)


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null= True)
    address_type = models.CharField(max_length=120, choices= ADDRESS_TYPE)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length= 120, null =True, blank = True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default = 'United States of America')

    def __str__(self):
        return str(self.profile)




