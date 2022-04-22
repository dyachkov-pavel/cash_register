from django.urls import path
from .views import generate_cheque

urlpatterns = [
    path('cash_machine/', generate_cheque, name='generate_cheque'),
]
