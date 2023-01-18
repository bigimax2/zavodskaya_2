# Данные функции созданы только для расчёта стоимости работ, расходников и общей цены заказа

from service_2.models import Jobs, Consumers, Orders


def cost_job(id_order):
    job = Jobs.objects.filter(order_id=id_order).values_list('jobs_price', flat=True)
    b = []
    x = 0
    for j in job:
        b.append(j)
    x += sum(b)
    return x


def cost_cons(id_jobs):
    consum = Consumers.objects.filter(job_id=id_jobs).values_list('consumers_price', flat=True)
    b = []
    x = 0
    for j in consum:
        b.append(j)
    x += sum(b)
    return x


def cost_cons_in_order(id_order):
    cust = Consumers.objects.filter(order_id=id_order).values_list('consumers_price', flat=True)
    c = []
    y = 0
    for a in cust:
        c.append(a)
    y += sum(c)
    return y


def all_cost(id_order):
    job = cost_job(id_order)
    cons = cost_cons_in_order(id_order)

    all_price = (job + cons)
    return all_price


def prepayment(id_order):
    prepay = Orders.objects.filter(id_order=id_order).values_list('prepayment', flat=True)
    c = []
    y = 0
    for a in prepay:
        c.append(a)
    y += sum(c)
    return y
