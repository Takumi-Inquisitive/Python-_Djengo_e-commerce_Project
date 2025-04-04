from django.contrib import admin
from .models import Product, Category, Cart, Order, Payment # Import your model
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock_qt']
    list_filter = ['category']
    search_fields = ['name', 'category']
    list_per_page = 5

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'is_paid']
    list_filter = ['is_paid']
    search_fields = ['user__username']

# Register your models here.
admin.site.register(Product, productAdmin)

admin.site.register(Category) 

admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
