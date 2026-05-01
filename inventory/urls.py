from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # لوحة التحكم الرئيسية
    path('', views.dashboard_inventory, name='dashboard'),

    # إدارة المنتجات
    path('produits/', views.produits_list, name='produits_list'),
    path('produits/<int:pk>/', views.produit_detail, name='produit_detail'),

    # مراقبة الصلاحية
    path('lots-expiring/', views.lots_expiring, name='lots_expiring'),

    # حركات المخزون
    path('mouvements/', views.mouvements_stock, name='mouvements_stock'),

    # التنبيهات
    path('alertes/', views.alertes_stock, name='alertes_stock'),

    # التقارير
    path('rapport-inventaire/', views.rapport_inventaire, name='rapport_inventaire'),

    # API endpoints
    path('api/produit/<int:pk>/stock/', views.api_produit_stock, name='api_produit_stock'),
    path('api/lots-expiring/', views.api_lots_expiring, name='api_lots_expiring'),
    path('api/alertes-non-lues/', views.api_alertes_non_lues, name='api_alertes_non_lues'),
    path('api/alerte/<int:pk>/marquer-lue/', views.marquer_alerte_lue, name='marquer_alerte_lue'),
]
