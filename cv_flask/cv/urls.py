from .views import CVHomePage
from django.urls import path

urlpatterns = [
    path('cv/', CVHomePage, name='CVHomePage'),
    # path('api/', api_home, name='api_home'),
]
