from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # user personal info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20)
    store_name = models.CharField(max_length=20)

    # address
    country = models.CharField(max_length=20, default="Nepal")
    city = models.CharField(max_length=20, default="Kathmandu")
    street = models.CharField(
        max_length=50, default="Please Update Your Sreet")
    landmark = models.CharField(
        max_length=50, default="Please Update Your Sreet")

    def __str__(self):
        return self.user.username
