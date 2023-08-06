from django.urls import path

from service_2 import views


urlpatterns = [
            path('', views.index, name='index'),
            path('allorders/', views.all_orders, name='allorders'),
            path('neworders/', views.NewOrder, name='neworder'),
            path('allorders/editeorder/<int:id_order>/', views.EditeOrder, name='editeorder'),
            path('allorders/deleteorder/<int:id_order>/', views.DeleteOrder, name='deleteorder'),
            path('allorders/jobsedite/<int:id_order>/', views.JobsOrder, name='jobsedite'),
            path('allorders/jobsedite/<int:order_id>/editeconsumers/<int:id_jobs>/', views.EditeConsumers,
                 name='jobsediteconsumers'),
            path('allorders/jobsedite/<int:order_id>/editeworker/<int:id_jobs>/', views.WorkerCreate,
                 name='editeworker'),
            path('logout/', views.logout_view, name='logout'),
]
