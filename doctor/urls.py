from django.urls import path
from doctor import views

urlpatterns = [
    path('', views.doctor, name='doctor'),

]

