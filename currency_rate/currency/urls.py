from django.urls import path
from currency.views import rate

urlpatterns = [
    path('rate/', rate, name='rate')
]
