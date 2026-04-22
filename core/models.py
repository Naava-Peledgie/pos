from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    loyalty_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} by {self.cashier.username}"
    

class SaleItem(models.Model):
    # Links this specific item to a single receipt/sale
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    
    # Links to the product being bought
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # How many of this product are being purchased
    quantity = models.PositiveIntegerField(default=1)
    
    # Stores the price at the exact moment of purchase
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    @property
    def get_total(self):
        return self.price_at_sale * self.quantity
    
    class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50, unique=True, blank=True, null=True) # Add this
    # ... keep your other fields (price, stock, etc.)