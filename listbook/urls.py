from django.urls import path 
from .views import IndexPageView,  menuView, mostrar, datosform_view, widget_view

urlpatterns = [ 
    path('', IndexPageView.as_view(), name='index'), 
    path('menu/', menuView, name='menu'), 
    path('listbook/', mostrar, name='listbook'),
    path('mostrar/', mostrar, name='mostrar'), 
    path('datosform/', datosform_view, name='datos_form'), 
    path('inputbook/', widget_view, name='widgetform'), 
    ]