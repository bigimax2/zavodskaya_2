from django.db import models
from django.urls import reverse


class Orders(models.Model):
    STATUS = [
        ('active', 'активный'),
        ('inactive', 'архив'),
    ]
    id_order = models.AutoField(primary_key=True)
    reg_num = models.CharField(max_length=12, blank=False, null=True, verbose_name='госномер')
    color = models.CharField(max_length=10, blank=True, null=True, verbose_name='цвет авто')
    time_create = models.DateField(auto_now_add=True, null=True)
    order_comments = models.CharField(max_length=255, blank=True, null=True, verbose_name='заметки по заказу')
    order_owner = models.CharField(max_length=20, blank=True, null=True, verbose_name='контакт')
    phone_owner = models.CharField(max_length=20, blank=True, null=True, verbose_name='тел. для связи')
    brand = models.CharField(max_length=20, blank=True, null=True, verbose_name='марка')
    model = models.CharField(max_length=20, blank=True, null=True, verbose_name='модель')
    vin = models.CharField(max_length=20, blank=True, null=True, verbose_name='VIN номер')
    status = models.CharField(choices=STATUS, max_length=20, default='active', verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.reg_num)

    def get_absolute_url(self):
        return reverse('allorders')


class Jobs(models.Model):
    id_jobs = models.AutoField(primary_key=True, blank=True)
    jobs_comments = models.CharField(max_length=255, null=True, blank=True, verbose_name='Вид работ:')
    jobs_price = models.IntegerField(null=True, blank=True,verbose_name='Цена')
    file = models.FileField(blank=True, null=True, upload_to='media/file', verbose_name='Поле для вставки файла ')
    image = models.ImageField(blank=True, null=True, upload_to='media/image', verbose_name='Поле для вставки фото')
    date_job = models.DateField(auto_now_add=True, null=True, blank=True)
    order = models.ForeignKey(Orders, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Работы по заказу'
        verbose_name_plural = 'Работы по заказу'

    def __str__(self):
        return str(self.jobs_comments)


class Consumers(models.Model):
    id_consumers = models.AutoField(primary_key=True, blank=True)
    consumers_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='наименование')
    consumers_price = models.IntegerField(null=True, blank=True, verbose_name='цена')
    consumers_quantity = models.IntegerField(null=True, blank=True, verbose_name='колл-во.')
    job = models.ForeignKey(Jobs, null=True, on_delete=models.CASCADE, verbose_name='выбрать вид работ')
    order = models.ForeignKey(Orders, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Расходники'
        verbose_name_plural = 'Расходники'

    def __str__(self):
        return str(self.consumers_name)
