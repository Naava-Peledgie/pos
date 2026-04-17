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
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE) [cite: 11]
    
    # Links to the product being bought
    product = models.ForeignKey(Product, on_delete=models.CASCADE) [cite: 9, 11]
    
    # How many of this product are being purchased
    quantity = models.PositiveIntegerField(default=1) [cite: 11]
    
    # Stores the price at the exact moment of purchase
    # This prevents old receipts from changing if you update product prices later
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2) [cite: 9]

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    @property
    def get_total(self):
        # Helper method to calculate the total price for this specific line item
        return self.price_at_sale * self.quantity   
