from django.contrib import admin
from .models import *

admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product']

admin.site.register(Order, OrderAdmin)