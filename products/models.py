from django.db import models

from crm_administration.models import SoftDelete




class Category(SoftDelete):
    """ table that contain possible category of product """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryRelations(models.Model):
    """ save all category relations, like products -> tablets """
    category = models.ForeignKey(Category, related_name='related_to_category', null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey(Category, related_name='related_to_parent', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.category.name


class Product(SoftDelete):
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
    language = models.SmallIntegerField(null=True)
    value = models.TextField()


class ProductImages(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='uploads/')
