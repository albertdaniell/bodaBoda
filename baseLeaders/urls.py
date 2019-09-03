from django.urls import path
from . import views

urlpatterns = [
    path('api/leaders/', views.leaders_list),
    path('api/leaders/<Email>/', views.leader_detail),
    path('api/leaders2/<int:id>/', views.leader_detail2),
    path('api/bases/', views.base_list),
    path('api/bases/<int:id>/', views.base_detail),
    path('api/bases1/<base_leader>/', views.base_detail2),
    
]