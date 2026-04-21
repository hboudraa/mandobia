from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('personnes/', views.liste_personnes, name='liste_personnes'),
    path('personnes/ajouter/', views.ajouter_personne, name='ajouter_personne'),
    path('personnes/<int:pk>/', views.detail_personne, name='detail_personne'),
    path('personnes/<int:pk>/modifier/', views.modifier_personne, name='modifier_personne'),
    path('personnes/<int:pk>/supprimer/', views.supprimer_personne, name='supprimer_personne'),
    path('personnes/exporter/', views.exporter_excel, name='exporter_excel'),
]
