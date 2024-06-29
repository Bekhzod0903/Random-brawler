from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random-brawler/', views.random_brawler_view, name='random_brawler'),

    # other paths
]
