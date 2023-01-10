from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True, db_index=True)
    cats = models.ManyToManyField(
        'Category', blank=True, related_name='products')
    image = models.ImageField(
        upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-pk', ]


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat_detail_url', kwargs={'pk': self.pk})


class Order(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    email = models.EmailField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
