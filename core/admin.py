from django.contrib import admin
from .models import Product, Customer, Sale, SaleItem

# 1. Advanced Registration for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Adds columns for price and stock to the list view 
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created_at')
    
    # Adds a search bar for finding products quickly 
    search_fields = ('name', 'category')
    
    # Adds a sidebar filter 
    list_filter = ('category',)

# 2. Basic Registration for other models
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleItem)