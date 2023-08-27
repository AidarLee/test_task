from django.urls import path
from .views import ProductListView, ProductExportView

urlpatterns = [
    path('all/', ProductListView.as_view(), name='product-list'),
    path('export/', ProductExportView.as_view(), name='product-export'),
]