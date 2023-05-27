from django.urls import path
from . import views

urlpatterns = [
    path('pengguna/', views.pengguna, name="pengguna"),
]