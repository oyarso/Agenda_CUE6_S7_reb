from django.views.generic import TemplateView 
from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .forms import WidgetForm 

def widgetform_view(request): 
    return render(request, "widgetform.html") 

class Libro(object): 
    def __init__ (self, titulo, autor, valoracion): 
        self.titulo=titulo 
        self.autor=autor   
        self.valoracion=  valoracion 

class IndexPageView(TemplateView): 
    template_name = "index.html" 
    
def menuView(request): 
    template_name = 'menu.html' 
    return render(request, template_name) 

def mostrar(request): 
    libro1 = Libro("Django 3 Web Development Cookbook Fourth Edition", "Aidas Bendoraitis", 3250)
    libro2 = Libro("Two Scoops of Django 3.x", "Daniel Feldroy", 1570)
    
    libro3 = Libro("Django for Professionals", "William S. Vincent", 2100)
    libro4 = Libro("Django for APIs", " William S. Vincent", 2540)

    libro5 = Libro("El libro de Django", "Adian Holovaty",0)
    libro6 = Libro("Python Web Development with Django", "Jeff Forcier",9) 

    items=[libro1,libro2,libro5,libro6,libro3,libro4]  



    context = {"items" : items} 
    return render(request, "templatesexample.html", context) 

def datosform_view(request): 
    context ={} 
    return render(request, "datosform.html", context) 


def widget_view(request): 
    context = {} 
    form = WidgetForm(request.POST or None) 
    context['form'] = form 
    return render(request, "widget_home.html", context) 