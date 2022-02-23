from django.urls import path, include
from api.Categories.views import CategoriesView
from api.Products.views import ProductsView
from api.Users.views import UserView

urlpatterns = [
    path('auth/', include("api.Auth.urls")),
    # path('user/', include('api.Users.urls')),
    # path('categories', include('api.Categories.urls')),
    # path('products/', include('api.Products.urls'))
    path('user', UserView.as_view()),
    path('categories', CategoriesView.as_view()),
    path('products', ProductsView.as_view())
]