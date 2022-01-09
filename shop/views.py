from django.shortcuts import render

# Create your views here.


def shop(request):
    data = {}
    return render(request, 'shop/shop.html', data)


def cart(request):
    data = {}
    return render(request, 'shop/cart.html', data)


def checkout(request):
    data = {}
    return render(request, 'shop/checkout.html', data)
