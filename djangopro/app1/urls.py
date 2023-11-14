from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proveedores/', views.lis_prov, name='list_prov'),
    path('add_prov/', views.view_form_prov, name='form_prov'),
]


