from django import forms 

class WidgetForm(forms.Form): 
    Titulo = forms.CharField(max_length = 150) 
    Autor = forms.CharField(max_length = 150) 
    Valoracion = forms.IntegerField(min_value=0, max_value=10000)  

