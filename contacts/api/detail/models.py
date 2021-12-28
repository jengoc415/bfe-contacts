from django.db import models

# Create your models here.


class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=254, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
