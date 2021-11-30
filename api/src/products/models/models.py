from api.src.authentication.models import User
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=80, unique=False, blank=False)
    price = models.DecimalField(max_digits=12, unique=False, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Files(models.Model):
    my_file = models.FileField(upload_to='file')
    file_type = models.CharField(max_length=35)
