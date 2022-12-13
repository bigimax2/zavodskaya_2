from django.db import models


class ModelCar(models.Model):
    id_model = models.AutoField(primary_key=True)
    model = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.model


class BrandCar(models.Model):
    id_brand = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.brand


class Status(models.Model):
    STATUS = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]
    id_status = models.AutoField(primary_key=True)
    status = models.CharField(choices=STATUS, max_length=20, default='active', verbose_name='Статус заказа')

    def __str__(self):
        return self.status


class OwnerCar(models.Model):
    id_owner = models.AutoField(primary_key=True)
    firstname_owner = models.CharField(max_length=20, null=True)
    lastname_owner = models.CharField(max_length=20, null=True, blank=True)
    phone_owner = models.CharField(max_length=11, null=True)
    email_owner = models.EmailField(max_length=20, null=True, blank=True)
    comments_owner = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.firstname_owner


class VinCar(models.Model):
    id_vin = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=18, null=True, blank=True)

    def __str__(self):
        return self.vin


class RegNumCar(models.Model):
    id_reg = models.AutoField(primary_key=True, blank=True)
    reg_num = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.reg_num


class Orders(models.Model):
    id_order = models.AutoField(primary_key=True)
    color = models.CharField(max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    model_car = models.ForeignKey(ModelCar, null=True, blank=True, on_delete=models.CASCADE)
    brand_car = models.ForeignKey(BrandCar, null=True, blank=True, on_delete=models.CASCADE)
    status_order = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE)
    owner_car = models.ForeignKey(OwnerCar, null=True, blank=True, on_delete=models.CASCADE)
    vin_car = models.ForeignKey(VinCar, null=True, blank=True, on_delete=models.CASCADE)
    regnum_car = models.ForeignKey(RegNumCar, null=True, blank=True, on_delete=models.CASCADE)
    order_comments = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.id_order


class Jobs(models.Model):
    id_jobs = models.AutoField(primary_key=True, blank=True)
    order_jobs = models.ManyToManyField(Orders, blank=True)
    jobs_comments = models.CharField(max_length=255, null=True, blank=True)
    jobs_price = models.IntegerField(null=True, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='media/file')
    image = models.ImageField(blank=True, null=True, upload_to='media/image')
    date_job = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.jobs_comments


class Consumers(models.Model):
    id_consumers = models.AutoField(primary_key=True, blank=True)
    jobs_consumers = models.ManyToManyField(Jobs, blank=True)
    consumers_name = models.CharField(max_length=20, null=True, blank=True)
    consumers_price = models.IntegerField(null=True, blank=True)
    consumers_quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.consumers_name
