from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=250, db_index=True)
    product_description = models.TextField(blank=True, db_index=True)
    product_price = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='products')

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_list_url', kwargs={'pk': self.pk})

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

