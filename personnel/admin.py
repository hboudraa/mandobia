from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Personne


# ── Personne ──────────────────────────────────────────────────────────
@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display  = ['nom', 'prenom', 'categorie', 'nin', 'telephone', 'wilaya', 'actif']
    list_filter   = ['categorie', 'wilaya', 'actif', 'role_systeme']
    search_fields = ['nom', 'prenom', 'nin', 'telephone']
    list_editable = ['actif']
    ordering      = ['nom', 'prenom']


# ── User (réenregistrement avec affichage complet) ────────────────────
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display  = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'date_joined']
    list_filter   = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering      = ['username']
    list_editable = ['is_active']

    fieldsets = (
        ('بيانات الدخول',     {'fields': ('username', 'password')}),
        ('المعلومات الشخصية', {'fields': ('first_name', 'last_name', 'email')}),
        ('الصلاحيات',         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('التواريخ',          {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email',
                       'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
