from django.contrib import admin
from .models import SuiviBaldiya, Tache, SuiviTache

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display  = ['nom', 'description', 'ordre', 'actif', 'cree_le']
    list_filter   = ['actif']
    search_fields = ['nom', 'description']
    ordering      = ['ordre', 'nom']
    list_editable = ['ordre', 'actif']

@admin.register(SuiviTache)
class SuiviTacheAdmin(admin.ModelAdmin):
    list_display  = ['baldiya', 'tache', 'statut', 'attribue_a', 'date_debut', 'date_fin', 'modifie_par', 'modifie_le']
    list_filter   = ['statut', 'tache', 'attribue_a', 'date_debut', 'date_fin']
    search_fields = ['baldiya__commune', 'tache__nom', 'remarque']
    ordering      = ['baldiya', 'tache__ordre']
    raw_id_fields = ['baldiya', 'tache']

@admin.register(SuiviBaldiya)
class SuiviBaldiyaAdmin(admin.ModelAdmin):
    list_display  = ['commune', 'get_commune_display', 'statut', 'attribue_a', 'modifie_par', 'modifie_le']
    list_filter   = ['statut', 'attribue_a']
    search_fields = ['wilaya']
    ordering      = ['commune']
