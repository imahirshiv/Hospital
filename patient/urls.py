from django.urls import path
from patient import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),    
    # path('about/', views.about, name='home_about'),

]

