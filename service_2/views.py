from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from service_2.forms import Order, JobsForm, Cons, WorkerForm
from service_2.models import Orders, Jobs, Consumers, Workers
from service_2.tables import JobTable, ConsumTable, WorkerTable
from service_2.utils import cost_job, cost_cons, cost_cons_in_order, all_cost, prepayment


# рендерит шаблон с главной страницей
def index(request, *args, **kwargs):
    return render(request, 'index.html')


# рендерит список всех заказов
def all_orders(request, *args, **kwargs):
    all = Orders.objects.all()
    return render(request, 'allorders.html', {'all': all})

#  рендерит форму нового заказа
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


# Редактирует данные о самом заказе, если ошибочно внесли данные или нужно дополнить
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


# Удаляет заказ из БД ,без удаления файлов и фото (их удалять вручную)
def DeleteOrder(request, id_order):
    try:
        order_del = Orders.objects.get(id_order=id_order)
        order_del.delete()
        return redirect('allorders')
    except Orders.DoesNotExist:
        return HttpResponseNotFound('<h2>Запись не найдена</h2>')


# Рендерит данные стоимости работ,расходников и общей цены ,а так же форму внесения данных о работах в заказ, в шаблон.
def JobsOrder(request, id_order):
    cost = cost_job(id_order)
    cost_cons = cost_cons_in_order(id_order)
    all_price = all_cost(id_order)
    pay = prepayment(id_order)


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
                                              'context': context, 'joborder': joborder, 'cost': cost,
                                              'cost_cons': cost_cons, 'all_price': all_price, 'pay': pay})


# Рендерит в шаблон таблицы цен, данные о заказе, форму внесения данных о расходниках
def EditeConsumers(request, id_jobs, order_id):
    cost_con = cost_cons(id_jobs)   # Импорт функции cost_cons() из utils c переменной id_jobs
    pay = prepayment(order_id)

    order = Orders.objects.get(id_order=order_id)   # Вносит в переменную order все объекта модели Orders по фильтру order_id
    job_order = Jobs.objects.get(id_jobs=id_jobs)   # ---- такая-же ботва,только с моделью Jobs и переменной id_jobs


    consum = ConsumTable(Consumers.objects.filter(job_id=id_jobs)) # Вносит в переменную consum таблицу ConsumTable из tabls с филтром id_jobs
                                                                   # это нужно для рендеринга формы записи расходников


    reg_num = order.reg_num     # вытаскиваем данные по заказу из переменной order для отправки в шаблон и там перебираем
    brand = order.brand         # ---------------------------------------------------------------------------------------
    moel = order.model          # ---------------------------------------------------------------------------------------
    color = order.color         # ---------------------------------------------------------------------------------------
    owner = order.order_owner   # ---------------------------------------------------------------------------------------
    phone = order.phone_owner   # ---------------------------------------------------------------------------------------

    context = [reg_num, brand, moel, color, owner, phone]

    consform = Cons                             # для рендеринга формы в шаблоне
    if request.method == 'POST':
        consform = Cons(request.POST)
        if consform.is_valid():
            post = consform.save(commit=False)
            post.job_id = id_jobs
            post.order_id = order_id
            post.save()
            return redirect('jobsediteconsumers', id_jobs=id_jobs, order_id=order_id)

    return render(request, 'editeconsumers.html', {'consform': consform, 'consum': consum, 'id_jobs': id_jobs,
                                                   'order_id': order_id, 'job_order': job_order, 'context': context,
                                                   'cost_con': cost_con, 'pay': pay})


# рендерит вход/выход
class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context['error'] = 'Invalid username or password'
        return render(request, self.template_name, context)


def WorkerCreate(request, id_jobs, order_id):

    worker = Jobs.objects.get(id_jobs=id_jobs)
    workertable = WorkerTable(Workers.objects.filter(job_id=worker))
    pay = prepayment(order_id)

    workform = WorkerForm
    if request.method == 'POST':
        workform = WorkerForm(request.POST)
        if workform.is_valid():
            post = workform.save(commit=False)
            post.job_id = id_jobs
            post.save()
            return redirect('editeworker', id_jobs, order_id)
    return render(request, 'editeworker.html', {'workform': workform, 'workertable': workertable,
                                                'order_id': order_id, 'pay': pay})
