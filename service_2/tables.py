import django_tables2 as tables
from django_tables2.utils import A

from service_2.models import Orders, Jobs, Consumers


class OrderTable(tables.Table):
    class Meta:
        model = Orders
        fields = ()


class JobTable(tables.Table):
    cons = tables.LinkColumn("jobsediteconsumers", text="Добавить", args=[A('order_id'), A('id_jobs')], verbose_name='Расходники')

    class Meta:
        model = Jobs
        template_name = "django_tables2/bootstrap.html"
        fields = ('jobs_comments', 'jobs_price', 'file', 'image', 'date_job')


class ConsumTable(tables.Table):
    class Meta:
        model = Consumers
        template_name = "django_tables2/bootstrap.html"
        fields = ('consumers_name', 'consumers_price', 'consumers_quantity')
