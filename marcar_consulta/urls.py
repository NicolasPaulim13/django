from django.urls import path
from . import views

urlpatterns = [
    path('marcar_consulta/', views.marcar_consulta, name='marcar_consulta'),
]
