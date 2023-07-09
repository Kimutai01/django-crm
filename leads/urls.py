from .import views
from django.urls import path


urlpatterns = [
    path('', views.lead_list, name='leads'),
    path('<str:pk>/', views.lead_detail, name='lead')
]
