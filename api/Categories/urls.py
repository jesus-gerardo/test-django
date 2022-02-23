from django.urls import path
from .views import CategoriesView

urlpatterns = [
    path('', CategoriesView.as_view())
    # path('/', CategoriesView.get),
    # path('store', CategoriesView.post),
    # path('<int:id>/update', CategoriesView.put),
    # path('<int:id>/delete', CategoriesView.delete)
]