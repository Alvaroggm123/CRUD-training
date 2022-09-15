from django.urls import path

# Our libs import
from . import views

urlpatterns = [
    path('', views.home),
    path('account/', views.account),
]
