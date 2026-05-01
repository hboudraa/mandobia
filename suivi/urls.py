from django.urls import path
from . import views

app_name = 'suivi'

urlpatterns = [
    path('',                   views.tableau_bord,      name='tableau_bord'),
    path('<int:pk>/modifier/', views.modifier_commune,  name='modifier'),
    path('<int:pk>/rapide/',   views.mise_a_jour_rapide, name='rapide'),
    path('<int:pk>/assigner/', views.assigner_commune,  name='assigner'),
    path('exporter/',          views.exporter_excel,    name='exporter_excel'),

    # إدارة المهام
    path('taches/',                    views.gestion_taches,        name='gestion_taches'),
    path('taches/<int:pk>/supprimer/', views.supprimer_tache,       name='supprimer_tache'),
    path('<int:commune_pk>/taches/',   views.suivi_taches_commune,  name='suivi_taches_commune'),
    path('<int:commune_pk>/taches/<int:tache_pk>/assigner/', views.assigner_tache, name='assigner_tache'),
    path('rapport-taches/',            views.rapport_taches,        name='rapport_taches'),

    # API للمهام
    path('<int:commune_pk>/taches-api/', views.get_commune_tasks_api, name='get_commune_tasks_api'),
    path('<int:commune_pk>/taches/<int:task_pk>/update/', views.update_task_status, name='update_task_status'),
    path('<int:commune_pk>/taches/<int:task_pk>/delete/', views.delete_task, name='delete_task'),
]
