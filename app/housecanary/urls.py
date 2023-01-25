from django.urls import path
from . import views

urlpatterns = [
    path('property/septic', views.get_have_septic, name='septic_verifier')
]