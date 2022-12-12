from django.db import models


class ModelCar(models.Model):
    id_model = models.AutoField(primary_key=True, null=True)
    model = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.model


class BrandCar(models.Model):
    id_brand = models.AutoField(primary_key=True, null=True)
    brand = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.brand


class Status(models.Model):
    STATUS = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]
    id_status = models.AutoField(primary_key=True, null=True)
    status = models.CharField(choices=STATUS, max_length=20, default='active', verbose_name='Статус заказа')

    def __str__(self):
        return self.status


class OwnerCar(models.Model):
    id_owner = models.AutoField(primary_key=True, null=True)
    firstname_owner = models.CharField(max_length=20, null=True)
    lastname_owner = models.CharField(max_length=20, null=True, blank=True)
    phone_owner = models.CharField(max_length=11, null=True)
    email_owner = models.EmailField(max_length=20, null=True, blank=True)
    comments_owner = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.firstname_owner


class VinCar(models.Model):
    id_vin = models.AutoField(primary_key=True, null=True)
    vin = models.CharField(max_length=18, null=True, blank=True)

    def __str__(self):
        return self.vin


class RegNumCar(models.Model):
    id_reg = models.AutoField(primaryKey=True, null=True, blank=True)
    reg_num = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.reg_num


class Orders(models.Model):
    id_order = models.AutoField(primary_key=True, null=True)
    color = models.CharField(max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    model_car = models.ForeignKey(ModelCar, null=True, blank=True, on_delete=models.CASCADE)
    brand_car = models.ForeignKey(BrandCar, null=True, blank=True, on_delete=models.CASCADE)
    status_order = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE)
    owner_car = models.ForeignKey(OwnerCar, null=True, blank=True, on_delete=models.CASCADE)
    vin_car = models.ForeignKey(VinCar, null=True, blank=True, on_delete=models.CASCADE)
    regnum_car = models.ForeignKey(RegNumCar, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_order
