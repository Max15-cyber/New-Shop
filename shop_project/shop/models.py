from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=250, db_index=True)
    product_description = models.TextField(blank=True, db_index=True)
    product_price = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

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