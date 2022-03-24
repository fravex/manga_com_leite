from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicamentos, name='lista_medicamentos'),
    path('exibe_medicamento/<int:id>/', views.exibe_medicamento, name='exibe_medicamento'),
    path('redireciona_anvisa/', views.redireciona_anvisa, name='redireciona_anvisa'),
    path('busca_anvisa/', views.busca_anvisa, name='busca_anvisa'),
]