from django.urls import path
from nduthiApp import views

urlpatterns = [
    path('api/rider/', views.rider_list),
     path('api/owner/', views.owner_list),
      path('api/vehicle/', views.vehicle_list),
       path('api/insurance/', views.insurance_list),
        path('api/sacco/', views.sacco_list),
    # path('api/restaurant_food/', views.restaurants_food),
    # path('api/restaurants/<int:pk>/', views.restaurant_detail),
    
]