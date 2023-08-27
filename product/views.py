from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from openpyxl import Workbook
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

class ProductListView(APIView):
    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request, *args, **kwargs):
        cache_key = 'product_list'
        cached_data = cache.get(cache_key)

        if cached_data is None:
            products = Product.objects.select_related('category', 'tag').all()
            serializer = ProductSerializer(products, many=True)
            cached_data = serializer.data
            cache.set(cache_key, cached_data)

        return Response(cached_data)
    
class ProductExportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()

        wb = Workbook()
        ws = wb.active

        ws.append(["ID", "Name", "Description", "Category", "Price", "Created At"])

        for product in products:
            ws.append([
                product.id,
                product.product_name,
                product.description,
                product.category.category_name,
                product.price,
                product.added_date.replace(tzinfo=None),
            ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=products.xlsx'

        wb.save(response)

        return response


        
        