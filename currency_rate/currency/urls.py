from django.urls import include, path
from currency.views import test_view

urlpatterns = [
    path('rate/', test_view, )
]
