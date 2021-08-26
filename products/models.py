from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)


class CategoryType(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_type = models.ForeignKey(CategoryType, null=True, blank=True, on_delete=models.CASCADE)
