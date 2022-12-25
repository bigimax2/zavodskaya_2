import django_tables2 as tables

from service_2.models import Orders

class OrderTable(tables.Table):
    class Meta:
        model = Orders
        fields = ()