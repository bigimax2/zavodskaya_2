import django_tables2 as tables

from service_2.models import Orders, Jobs, Consumers


class OrderTable(tables.Table):
    class Meta:
        model = Orders
        fields = ()


class JobTable(tables.Table):
    c_name = tables.TemplateColumn('<a href="{% url "jobsediteconsumers" record.id_jobs %}"{{order_id}}>Добавить</a>', verbose_name='Расходники')

    class Meta:
        model = Jobs
        template_name = "django_tables2/bootstrap.html"
        fields = ('id_jobs','jobs_comments', 'jobs_price', 'file', 'image', 'date_job', 'order_id')


class Consum(tables.Table):
    class Meta:
        model = Consumers
        template_name = "django_tables/bootstrap.html"
        fields = ('consumers_name', 'consumers_price', 'consumers_quantity')
