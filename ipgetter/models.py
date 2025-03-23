from django.db import models

class User(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    isp = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)  # Stores the timestamp of record creation

    def __str__(self):
        return f"{self.ip_address} - {self.country} - {self.city} - {self.isp} - {self.date_entered}"
