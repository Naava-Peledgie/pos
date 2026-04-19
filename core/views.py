from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product # Import your Product model

@login_required
def dashboard(request):
    # This line grabs every product you've added in the Admin
    products = Product.objects.all()
    
    # This counts how many items you have in total
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'core/dashboard.html', context)