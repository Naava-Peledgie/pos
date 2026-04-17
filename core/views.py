from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Sale

@login_required
def dashboard(request):
    # This will pull data for your dashboard summary later
    total_products = Product.objects.count()
    total_sales = Sale.objects.count()
    
    context = {
        'total_products': total_products,
        'total_sales': total_sales,
    }
    return render(request, 'core/dashboard.html', context)