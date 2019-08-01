from django.urls import path
from mpesaTransactions import views


urlpatterns = [
    path('api/payments/', views.payments),
    # path('snippets/<int:pk>/', views.snippet_detail),
]