from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.agendamento_list, name='agendamento_list'),
    path('consulta/', views.consulta_view, name='consulta'),
    path('editar/<int:pk>/', views.agendamento_update, name='agendamento_update'),
    path('excluir/<int:pk>/', views.agendamento_delete, name='agendamento_delete'),
]