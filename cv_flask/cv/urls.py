from .views import CVHomePage
from django.urls import path

urlpatterns = [
    path('', CVHomePage, name='CVHomePage'),
]
