from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('buy/', views.buy_filter),
    path('sell/', views.sell),
    path('buy/filter', views.buy_filter_2),
]
