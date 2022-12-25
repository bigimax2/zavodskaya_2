from django.contrib import admin

from .models import *


class JobsInLineAdmin(admin.TabularInline):
    model = Jobs


class ConsumersInLine(admin.TabularInline):
    model = Consumers


class OrdersAdmin(admin.ModelAdmin):
    inlines = [
        JobsInLineAdmin,
        ConsumersInLine,
    ]


admin.site.register(Orders, OrdersAdmin)

