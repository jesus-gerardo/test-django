from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login', LoginView.login),
    path('logout', LoginView.logout),
]
