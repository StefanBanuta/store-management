from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('', views.pagina_principala, name='pagina_principala'),

    path('sterge_client/<int:pk>/', views.sterge_client, name='sterge_client'),
    path('tabela-clienti/', views.tabela_clienti, name='tabela_clienti'),
    path('clienti/<int:client_id>/modifica/', views.modifica_client, name='modifica_client'),

    path('sterge_produs_alimentar/<int:pk>/', views.sterge_produs_alimentar, name='sterge_produs_alimentar'),
    path('produse-alimentare/', views.tabela_produse_alimentare, name='lista_produse_alimentare'),
    path('produse-alimentare/<int:produs_id>/modifica/', views.modifica_produs_alimentar, name='modifica_produs_alimentar'),

    path('tabela-producatori/', views.tabela_producatori, name='tabela_producatori'),
    path('producatori/<int:producator_id>/modifica/', views.modifica_producator, name='modifica_producator'),
    path('sterge_producator/<int:pk>/', views.sterge_producator, name='sterge_producator'),

    path('achizitii/', views.tabela_achizitii, name='tabela_achizitii'),
    path('sterge_achizitie/<int:pk>/', views.sterge_achizitie, name='sterge_achizitie'),
    path('modifica_achizitie/<int:achizitie_id>/', views.modifica_achizitie, name='modifica_achizitie'),


    path('comenzi/', views.tabela_comenzi, name='tabela_comenzi'),
    path('sterge_comanda/<int:pk>/', views.sterge_comanda, name='sterge_comanda'),
    path('comenzi/<int:comanda_id>/modifica/', views.modifica_comanda, name='modifica_comanda'),

    path('test/', views.test, name='test'),
]