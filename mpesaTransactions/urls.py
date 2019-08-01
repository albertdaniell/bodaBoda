from django.urls import path
from mpesaTransactions import views


urlpatterns = [
    path('api/payments/', views.payments),
    path('api/payments/<phoneNumber>/', views.payment_detail),
]