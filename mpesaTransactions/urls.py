from django.urls import path
from mpesaTransactions import views


urlpatterns = [
    path('api/payments/', views.payments),
    path('snippets/<phoneNumber>/', views.payment_detail),
]