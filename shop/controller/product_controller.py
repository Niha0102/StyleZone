from itertools import product

from django.http import request
from django.shortcuts import render
from decimal import Decimal
from shop.dao.implementation.product_dao import ProductDAO
from shop.model.product_model import Product


def product_list(request):

    dao = ProductDAO()

    category = request.GET.get('category')
    search = request.GET.get('search')
    color = request.GET.get('color')
    price_range = request.GET.get('price_range')
    sort = request.GET.get('sort')


    # Colours

    colors = list(
        Product.objects.values_list(
            'base_color',
            flat=True
        ).distinct().order_by('base_color')
    )


    # Start with all products

    products = dao.get_all_products()


    # Category filter

    if category == 'women':

        products = dao.get_products_by_category(1)

    elif category == 'men':

        products = dao.get_products_by_category(3)

    elif category == 'indian':

        products = dao.get_products_by_category(2)

    elif category == 'bestseller':

        products = dao.get_best_seller_products()


    # Search filter

    if search:

        products = products.filter(
            product_name__icontains=search
        )


    # Colour filter

    if color:

        products = products.filter(
            base_color__iexact=color
        )


    # Price range filter

    if price_range:

        if price_range == '0-499':

            products = products.filter(
                price__lt=500
            )

        elif price_range == '500-999':

            products = products.filter(
                price__gte=500,
                price__lte=999
            )

        elif price_range == '1000-1499':

            products = products.filter(
                price__gte=1000,
                price__lte=1499
            )

        elif price_range == '1500-1999':

            products = products.filter(
                price__gte=1500,
                price__lte=1999
            )

        elif price_range == '2000-2999':

            products = products.filter(
                price__gte=2000,
                price__lte=2999
            )

        elif price_range == '3000+':

            products = products.filter(
                price__gte=3000
            )


    # Sorting

    if sort == 'price_low':

        products = products.order_by('price')

    elif sort == 'price_high':

        products = products.order_by('-price')

    elif sort == 'name':

        products = products.order_by('product_name')

    else:

        products = products.order_by('product_id')

  
    return render(
        request,
        'shop/products.html',
        {
            'products': products,
            'search': search,
            'color': color,
            'price_range': price_range,
            'colors': colors,
            'sort': sort
        }
    )


def product_details(request, product_id):

    dao = ProductDAO()

    product = dao.get_product_by_id(product_id)

    discounted_price = product.price

    if product.discount_percent:
        discounted_price = product.price - (
            product.price * product.discount_percent / Decimal("100")
        )

    return render(
        request,
        'shop/product_details.html',
        {
            'product': product,
            'discounted_price': discounted_price
        }
    )
