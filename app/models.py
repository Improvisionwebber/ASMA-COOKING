# asma_app/models.py
from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Product {self.pk}"
