from django.urls import path

from . import views


urlpatterns = [

    path('lista/', views.productos),
    path('ingresar/', views.ingresar),
    path('addp/', views.addp),

]
