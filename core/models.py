from django.db import models

# 1. Product Model
class Product(models.Model):
    # Define categories for both the bakery and the boutique
    CATEGORY_CHOICES = [
        ('Bakery', 'Bakery'),
        ('Electronics', 'Electronics'),
        ('cosmetics', 'Cosmetics'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    
    # Using 'choices' creates the dropdown menu in the Admin panel
    category = models.CharField(
        max_length=100, 
        choices=CATEGORY_CHOICES, 
        default='General'
    )
    
    # Barcode field for Phase 6 scanning features
    barcode = models.CharField(max_length=50, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 2. Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

# 3. Sale Model
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.product.name} at {self.timestamp}"

# 4. SaleItem Model (For multiple items per receipt)
class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)