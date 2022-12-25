from django.urls import path

from service_2 import views


urlpatterns = [
            path('', views.index, name='index'),
            path('allorders/', views.all_orders, name='allorders'),
            path('neworders/', views.NewOrder, name='neworder'),
            path('allorders/editeorder/<int:id_order>/', views.EditeOrder, name='editeorder'),
            path('allorders/deleteorder/<int:id_order>/', views.DeleteOrder, name='deleteorder'),

]