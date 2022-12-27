import django_tables2 as tables

from service_2.models import Orders, Jobs




class OrderTable(tables.Table):
    class Meta:
        model = Orders
        fields = ()


class JobTable(tables.Table):
    c_name = tables.TemplateColumn('<a href="{% url "jobsediteconsumers" record.id_jobs %}">Edite</a>')

    class Meta:
        model = Jobs
        template_name = "django_tables2/bootstrap.html"
        fields = ('jobs_comments', 'jobs_price', 'file', 'image', 'date_job', 'c_name',)
