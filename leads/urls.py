from .import views
from django.urls import path


urlpatterns = [
    path('', views.lead_list, name='leads'),
    path('<int:pk>/', views.lead_detail, name='lead'),
    path('create/', views.lead_create, name='create-lead'),
    path('update/<int:pk>/', views.lead_update, name='update-lead'),
    path('delete/<int:pk>/', views.lead_delete, name='delete-lead')
]
