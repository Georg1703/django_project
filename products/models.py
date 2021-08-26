from django.db import models

from crm_administration.models import SoftDelete


class Product(SoftDelete):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(SoftDelete):
    """ table that contain possible category of product """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CategoryRelations(models.Model):
    pass


class ProductLang(models.Model):
    """ table that contain all possible language of product """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductLocalizationColumns(models.Model):
    """ table that contain all possible column of product that must be localize """
    name = models.CharField(max_length=100)


class ProductLocalization(models.Model):
    """ table for product localization """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    column_type = models.ForeignKey(ProductLocalizationColumns, on_delete=models.CASCADE)
    language = models.ForeignKey(ProductLang, null=True, on_delete=models.SET_NULL)
    value = models.TextField()
