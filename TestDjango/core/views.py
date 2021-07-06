from django.http import request
from django.shortcuts import render, redirect
from .models import DatosColaboradores
from .forms import ColabForm

# Create your views here.

def home(request):

    return render(request, 'home.html')

def Ver(request):
    vercolab= DatosColaboradores.objects.all()
    return render (request, 'core/ver.html',context={'vercolab':vercolab})
    
def form_colab(request):
    if request.method == 'POST': 
        colab_form = ColabForm(request.POST, files=request.FILES)
        if colab_form.is_valid():
            colab_form.save()        #similar al insert de un modelo relacional 
            return redirect('home')
    else: 
        colab_form = ColabForm()
    return render(request, 'core/form_colab.html', {'colab_form': colab_form})

def form_mod_colab(request,id):
    colab = DatosColaboradores.objects.get(rut=id)

    datos={
        'form': ColabForm(instance=colab)
    }
    if request.method == 'POST':
        formulario = ColabForm(data=request.POST, instance = colab, files= request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect ('ver')
    return render(request,'core/form_mod_colab.html',datos)

def form_del_colab(request,id):
    colab = DatosColaboradores.objects.get(rut=id)
    colab.delete()
    return redirect('ver')
    

