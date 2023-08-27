from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'price', 'added_date')
    search_fields = ['product_name', 'description'] 
    ordering = ['price', 'added_date'] 
    list_filter = ['category']
    date_hierarchy = 'added_date'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ['category_name']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')
    search_fields = ['tag_name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
