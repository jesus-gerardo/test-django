from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from api.Users.models import Users

# Create your views here.
class LoginView:
    def login(request):
        return JsonResponse({
            "response": True
        }, status=200)

    def logout(request):
        pass