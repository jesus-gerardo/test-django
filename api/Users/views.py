from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Users

# Create your views here.
class UserView:
    def index(request):
        return JsonResponse({
            "response": True
        }, status=200)

    def store(request):
        pass