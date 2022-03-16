from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from inventario.models import Servidor

class ServidorList(ListView):
    model = Servidor
    queryset = Servidor.objects.all()
    
class ServidorCreate(CreateView):
    model = Servidor
    fields = '__all__'
    success_url = reverse_lazy('inventario:list')
    
class ServidorUpdate(UpdateView):
    model = Servidor
    fields = '__all__'
    success_url = reverse_lazy('inventario:list')    
    
class ServidorDetail(DetailView):
    model = Servidor
    queryset = Servidor.objects.all()       
        
class ServidorDelete(DeleteView):
    model = Servidor
    queryset = Servidor.objects.all() 
    success_url = reverse_lazy('inventario:list')     

    


