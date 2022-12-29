from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin

from .models import *


class ConsumersInLine(NestedTabularInline):
    model = Consumers


class JobsInLine(NestedTabularInline):
    model = Jobs
    inlines = [ConsumersInLine]


class OrdersAdmin(NestedModelAdmin):
    inlines = [JobsInLine]


admin.site.register(Orders, OrdersAdmin)

