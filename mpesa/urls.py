from django.urls import path
from . import views

urlpatterns = [
    path('mpesa/', views.mpesa_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]