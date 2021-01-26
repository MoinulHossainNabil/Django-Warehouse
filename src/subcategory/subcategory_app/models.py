from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=100, null=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='parent')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey('Subcategory', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name


