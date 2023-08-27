from django.db import models
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Наименование категории")

    def __str__(self) -> str:
        return f"{self.category_name}"

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, verbose_name="Наименование тега")

    def __str__(self) -> str:
        return f"{self.tag_name}"


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('category', 'tag')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    price = models.FloatField(verbose_name="Цена товара")
    added_date = models.DateTimeField(verbose_name="Дата добавления", default=timezone.now)

    objects = ProductManager()

    def __str__(self) -> str:
        return f"{self.product_name}"

