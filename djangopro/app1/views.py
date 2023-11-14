from django.shortcuts import render,redirect
from .models import Proveedor
from .forms import form_proveedor as fp
from django.http import HttpResponseRedirect

def lis_prov(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def view_form_prov(request):
    if request.method == "POST":
        formulario = fp.ProvForm(request.POST)
        if formulario.is_valid():
            return HttpResponseRedirect("/")
    else:
        formulario = fp.ProvForm()
        return render(request,"Add_prov.html",{"form":formulario})

def home(request):
    return render(request,"home.html")