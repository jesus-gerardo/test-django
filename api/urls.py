from django.urls import path, include

urlpatterns = [
    path('auth/', include("api.Auth.urls")),
    path('user/', include('api.Users.urls'))
]