from django.db import models


class Orders(models.Model):
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=10)
    reg_num = models.CharField(max_length=8)
    owner = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    vin = models.CharField(max_length=18)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.reg_num
