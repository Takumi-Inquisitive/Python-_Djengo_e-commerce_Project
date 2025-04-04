from django.contrib import admin
from .models import Product, Category,Client, Invoice, InvoiceItem,  Cart, Order, Payment, StockReport

# Product Management
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock_qt']
    list_filter = ['category']
    search_fields = ['name', 'category']
    list_per_page = 5

# Order Management
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'is_paid']
    list_filter = ['is_paid']
    search_fields = ['user__username']

# Client Management
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')

# Invoice Management
class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1  

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'created_at')
    inlines = [InvoiceItemInline]  

# Stock Reports 
@admin.register(StockReport)
class StockReportAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock_in', 'stock_out', 'current_stock')
    readonly_fields = ('product', 'stock_in', 'stock_out', 'current_stock')  

# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
