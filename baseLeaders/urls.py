from django.urls import path
from . import views

urlpatterns = [
    path('api/leaders/', views.leaders_list),
    path('api/leaders/<Email>/', views.leader_detail),
    
]