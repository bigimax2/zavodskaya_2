
from django.forms import ModelForm
from django import forms
from django_select2 import forms as s2forms

from service_2.models import Orders, Jobs, Consumers, Workers


class AllOrders(ModelForm):
    class Meta:
        model = Orders(id_order='get_order')
        fields = '__all__'


class Order(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ['order', ]


class Cons(forms.ModelForm):
    class Meta:
        model = Consumers
        exclude = ['job', 'order']


class WorkWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "worker__contains",
    ]


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Workers
        fields = "__all__"
        widgets = {
            "worker": WorkWidget.model,
        }


