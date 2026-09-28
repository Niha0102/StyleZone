from django.shortcuts import render
from shop.dao.implementation.product_dao import ProductDAO
from shop.model.product_model import Product


def home(request):

    dao = ProductDAO()

    best_sellers = Product.objects.filter(
        product_id__in=[122, 79, 88, 58]
    )

    women_products = dao.get_products_by_category(1).exclude(
        product_name__icontains="Elegant Everyday Dress"
    ).exclude(
        product_name__icontains="Effortless Style Dress"
    ).exclude(
        product_name__icontains="Classic Casual Top"
    )

    indian_products = dao.get_products_by_category(2)

    men_products = dao.get_products_by_category(3)

    return render(request, 'shop/home.html', {
        'best_sellers': best_sellers,
        'women_products': women_products,
        'indian_products': indian_products,
        'men_products': men_products
    })