from django.contrib import admin
from .models import Product, Customer, Sale, SaleItem

# 1. Advanced Configuration for Products
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # These columns will show up in your inventory list
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created_at')
    
    # This adds a search bar that checks names, categories, and barcodes
    search_fields = ('name', 'category', 'barcode')
    
    # This adds a filter sidebar on the right
    list_filter = ('category',)
    
    # This makes the "created_at" date show up as a read-only field
    readonly_fields = ('created_at',)

# 2. Simple Registration for other models
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'timestamp')
    list_filter = ('timestamp', 'product')

# 3. Register SaleItem if you are using it
@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity', 'price_at_sale')