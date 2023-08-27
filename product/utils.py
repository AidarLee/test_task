from django.core.cache import cache

def clear_product_list_cache():
    cache_key = 'product_list'
    cache.delete(cache_key)