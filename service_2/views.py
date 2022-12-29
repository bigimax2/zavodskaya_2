from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from service_2.forms import Order, JobsForm, Cons
from service_2.models import Orders, Jobs
from service_2.tables import JobTable


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


def JobsOrder(request, id_order):
    joborder = Orders.objects.get(id_order=id_order)
    jobs = JobTable(Jobs.objects.filter(order_id=joborder))

    id = joborder.id_order
    reg_num = joborder.reg_num
    color = joborder.color
    comments = joborder.order_comments
    owner = joborder.order_owner
    phone = joborder.phone_owner
    brand = joborder.brand
    model = joborder.model
    context = [reg_num, color, comments, owner, phone, brand, model]



    jobform = JobsForm
    if request.method == 'POST':
        jobform = JobsForm(request.POST, request.FILES)
        if jobform.is_valid():
            post = jobform.save(commit=False)
            post.order_id = id_order
            post.save()

            return redirect('jobsedite', id_order=id_order)

    return render(request, 'jobsedite.html', {'jobform': jobform, 'jobs': jobs, 'id_order': id_order,
                                              'context': context, 'joborder': joborder})


def EditeConsumers(request, id_jobs):
    consform = Cons
    if request.method == 'POST':
        consform = Cons(request.POST)
        if consform.is_valid():
            post = consform.save(commit=False)
            post.job_id = id_jobs
            #post.order_id = id_order
            post.save()
            return redirect('jobsediteconsumers', id_jobs=id_jobs)

    return render(request, 'editeconsumers.html', {'consform': consform})
