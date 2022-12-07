from django.db import models


# Create your models here.


class Data(models.Model):
    name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    Address = models.TextField(null=True)
    product_name = models.CharField(max_length=30)

