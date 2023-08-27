from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .utils import clear_product_list_cache

@receiver(post_save, sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    clear_product_list_cache()