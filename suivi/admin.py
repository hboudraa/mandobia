from django.contrib import admin
from .models import SuiviBaldiya

@admin.register(SuiviBaldiya)
class SuiviBaldiyaAdmin(admin.ModelAdmin):
    list_display  = ['commune', 'get_commune_display', 'statut', 'attribue_a', 'modifie_par', 'modifie_le']
    list_filter   = ['statut', 'attribue_a']
    search_fields = ['wilaya']
    ordering      = ['commune']
