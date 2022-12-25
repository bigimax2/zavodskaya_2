from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from service_2.forms import Order
from service_2.models import Orders


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def all_orders(request, *args, **kwargs):
    all = Orders.objects.all()
    return render(request, 'allorders.html', {'all': all})


def NewOrder(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            try:
                Orders.objects.create(**form.cleaned_data)
                return redirect('allorders')
            except:
                form.add_error(None, 'Ошибка заполнения')
    else:
        form = Order()
    return render(request, 'neworder.html', {'form': form})


def EditeOrder(request, id_order):
    model = Orders.objects.get(id_order=id_order)
    form = Order(instance=model)

    if request.method == 'POST':
        forms = Order(request.POST, instance=model)
        if forms.is_valid():
            table = forms.save()
            table.save()
            return redirect('allorders')
        else:
            return HttpResponse('НЕ получилось')

    return render(request, 'editeorder.html', {'form': form, 'id_order': id_order, 'model': model})


def DeleteOrder(request, id_order):
    try:
        order_del = Orders.objects.get(id_order=id_order)
        order_del.delete()
        return redirect('allorders')
    except Orders.DoesNotExist:
        return HttpResponseNotFound('<h2>Запись не найдена</h2>')
