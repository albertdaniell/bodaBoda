from django.urls import path
from . import views

urlpatterns = [
    path('api/leaders/', views.leaders_list),
    path('api/leaders/<Email>/', views.leader_detail),
    path('api/leaders2/<int:id>/', views.leader_detail2),
    path('api/bases/', views.base_list),
    
]