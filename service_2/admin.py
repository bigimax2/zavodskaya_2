
# правильная регистрация моделей данного приложения,силами стандартной админки django не возможна, ввиду спецефичных связей между моделями

from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin
# Библиотека nested_inline не идёт из коробки джанго,почитать тут https://github.com/s-block/django-nested-inline
from .models import *


class WorkerInLine(NestedTabularInline):
    model = Workers
    extra = 0
    fk_name = 'job'


class ConsumersInLine(NestedTabularInline):
    model = Consumers
    extra = 0
    fk_mane = 'job'


class JobsInLine(NestedStackedInline):
    model = Jobs
    extra = 0
    fk_name = 'order'
    inlines = [ConsumersInLine, WorkerInLine]


class OrdersAdmin(NestedModelAdmin):
    inlines = [JobsInLine]


admin.site.register(Orders, OrdersAdmin)

