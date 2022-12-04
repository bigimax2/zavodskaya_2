from django.urls import path

from service_2 import views


urlpatterns = [
            path('', views.index, name='index'),
]

