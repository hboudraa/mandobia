from django.urls import path
from . import views

app_name = 'suivi'

urlpatterns = [
    path('',                   views.tableau_bord,      name='tableau_bord'),
    path('<int:pk>/modifier/', views.modifier_commune,  name='modifier'),
    path('<int:pk>/rapide/',   views.mise_a_jour_rapide, name='rapide'),
    path('<int:pk>/assigner/', views.assigner_commune,  name='assigner'),
    path('exporter/',          views.exporter_excel,    name='exporter_excel'),
]
