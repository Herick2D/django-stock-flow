from django.urls import path
from .views import TesteView

urlpatterns = [
    path('produtos/', TesteView.as_view(), name='produtos-list'),
]
