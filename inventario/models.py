from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Dominio(models.Model):
    nome  = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    
    def __str__(self):        
        return self.nome

class Responsavel(models.Model):
    nome  = models.CharField(max_length=255)
    
    def __str__(self):        
        return self.nome

class Ambiente(models.Model):
    nome  = models.CharField(max_length=255)
    
    def __str__(self):        
        return self.nome

class Operacional(models.Model):
    nome  = models.CharField(max_length=255)
    
    def __str__(self):        
        return self.nome

class Ferramenta(models.Model):
    nome  = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def __str__(self):        
        return self.nome

class Versao(models.Model):
    nome  = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def __str__(self):        
        return self.nome


class Pci(models.Model):
    nome  = models.CharField(max_length=50)

    def __str__(self):        
        return self.nome

class Externo(models.Model):
    nome  = models.CharField(max_length=50)
    
    def __str__(self):        
        return self.nome

class Vlan(models.Model):
    nome  = models.CharField(max_length=50)
    mascara  = models.CharField(max_length=50)
    gateway  = models.CharField(max_length=50)
    
    def __str__(self):        
        return self.nome        

class Contexto(models.Model):
    nome  = models.CharField(max_length=50)
    
    def __str__(self):        
        return self.nome

class Empresa(models.Model):
    nome  = models.CharField(max_length=50)
    
    def __str__(self):        
        return self.nome


class Url(models.Model):
    endereco = models.CharField(max_length=255)
    
    def __str__(self):        
        return self.endereco  


class Servidor(models.Model):
    nome = models.CharField(max_length=255)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    dominio = models.ForeignKey(Dominio, on_delete=models.CASCADE)
    ip = models.CharField(max_length=255)
    os = models.ForeignKey(Operacional, on_delete=models.CASCADE)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE)
    versao = models.ForeignKey(Versao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    pci = models.ForeignKey(Pci, on_delete=models.CASCADE)
    externo = models.ForeignKey(Externo, on_delete=models.CASCADE)
    vlan = models.ForeignKey(Vlan, on_delete=models.CASCADE)
    contexto = models.ForeignKey(Contexto, on_delete=models.CASCADE)
    disco = models.CharField(max_length=255)
    memoria = models.CharField(max_length=255)
    vcpu = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome   
    
    #def get_absolute_url(self):
    #    return reverse("servidor:detail", kwargs={"nome": self.nome})

    
class ServidorUrl(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    
    def __str__(self):        
        return self.servidor       
          
