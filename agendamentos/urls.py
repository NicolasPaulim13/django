from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.agendamento_list, name='agendamento_list'),
    path('novo/', views.agendamento_create, name='agendamento_create'),
    path('editar/<int:pk>/', views.agendamento_update, name='agendamento_update'),
    path('excluir/<int:pk>/', views.agendamento_delete, name='agendamento_delete'),
]