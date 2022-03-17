import csv
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from inventario.models import Servidor

def csv_database_write(request):
    
    # Get all data from UserDetail Databse Table
    servidores = Servidor.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Ambiente', 'Responsavel', 'Dominio'])

    for server in servidores:
        writer.writerow([server.nome, server.ambiente, server.responsavel, server.dominio])

    return response

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

    


