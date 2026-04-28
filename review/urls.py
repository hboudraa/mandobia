from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Review Periods
    path('periods/', views.review_periods_list, name='periods_list'),
    path('periods/add/', views.review_period_add, name='period_add'),
    path('periods/<int:pk>/edit/', views.review_period_edit, name='period_edit'),

    # Reviews
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('reviews/add/', views.review_add, name='review_add'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    path('reviews/<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),

    # Export
    path('export/excel/', views.export_reviews_excel, name='export_excel'),
]

