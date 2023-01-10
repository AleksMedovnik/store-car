from django.shortcuts import render
from .models import Product, Category, Order
from django.db.models import Q


def build_table(lst, cols):
    return [lst[i:i+cols] for i in range(0, len(lst), cols)]


def product_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(info__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    return render(request, 'store/store.html', context={'products_block': build_table(products, 3)})


def cat_list(request):
    cats = Category.objects.all()
    return render(request, 'store/cats.html', context={'cats': cats})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'store/product.html', context={'product': product})


def cat_detail(request, pk):
    cat = Category.objects.get(pk=pk)
    products = cat.products.all()
    return render(request, 'store/cat.html', context={'cat': cat, 'products_block': build_table(products, 3)})


def save_order(request):
    product = Product.objects.get(pk=request.POST['product_id'])
    order = Order()
    order.name = request.POST['username']
    order.name = request.POST['user_email']
    order.product = product
    order.save()
    return render(request, 'store/order.html', context={'product': product})