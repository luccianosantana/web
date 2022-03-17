from django.contrib import admin
from .models import *

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ("nome","dominio","ip")
    

@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
    list_display = ("nome","local")    

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)    

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ("nome",)        

@admin.register(Operacional)
class OperacionalAdmin(admin.ModelAdmin):
    list_display = ("nome",)        

@admin.register(Ferramenta)
class FerramentaAdmin(admin.ModelAdmin):
    list_display = ("nome",)  

@admin.register(Versao)
class VersaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)      

@admin.register(Pci)
class PciAdmin(admin.ModelAdmin):
    list_display = ("nome",)  

@admin.register(Externo)
class ExternoAdmin(admin.ModelAdmin):
    list_display = ("nome",)    

@admin.register(Vlan)
class VlanAdmin(admin.ModelAdmin):
    list_display = ("nome",)             

@admin.register(Contexto)
class ContextoAdmin(admin.ModelAdmin):
    list_display = ("nome",) 

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome",)      





    