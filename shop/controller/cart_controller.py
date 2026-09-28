from django.http import JsonResponse
from django.shortcuts import render

from shop.dao.implementation.cart_dao import CartDAO
from shop.dao.implementation.product_dao import ProductDAO
from shop.model.cart_item_model import CartItem

def add_to_cart(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Invalid request"
        })

    # Get logged-in user
    user_id = request.session.get("user_id")

    # Get product information
    product_id = request.POST.get("product_id")
    size_label = request.POST.get("size_label")
    quantity = request.POST.get("quantity")

    # Check login
    if not user_id:
        return JsonResponse({
            "success": False,
            "message": "Please login first"
        })

    # Check required information
    if not product_id or not size_label or not quantity:
        return JsonResponse({
            "success": False,
            "message": "Missing required information"
        })

    cart_dao = CartDAO()
    product_dao = ProductDAO()

    # Find user's cart
    cart = cart_dao.get_cart_by_user(user_id)

    # Create cart if it does not exist
    if not cart:
        cart = cart_dao.create_cart(user_id)

    # Get product
    product = product_dao.get_product_by_id(product_id)

    if not product:
        return JsonResponse({
            "success": False,
            "message": "Product not found"
        })

    # Add or update cart item
    cart_dao.add_or_update_cart_item(
        cart.cart_id,
        product.product_id,
        size_label,
        int(quantity),
        product.price
    )

    return JsonResponse({
        "success": True,
        "message": "Product added to cart"
    })

def cart(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return render(
            request,
            "shop/cart.html",
            {
                "cart_items": []
            }
        )

    cart_dao = CartDAO()
    product_dao = ProductDAO()

    user_cart = cart_dao.get_cart_by_user(user_id)

    if not user_cart:
        return render(
            request,
            "shop/cart.html",
            {
                "cart_items": []
            }
        )

    cart_items = cart_dao.get_cart_items(
        user_cart.cart_id
    )

    cart_products = []

    for item in cart_items:

        product = product_dao.get_product_by_id(
            item.product_id
        )

        cart_products.append({
            "cart_item": item,
            "product": product
        })

    return render(
        request,
        "shop/cart.html",
        {
            "cart_items": cart_products
        }
    )

def update_cart_quantity(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Invalid request"
        })

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({
            "success": False,
            "message": "Please login first"
        })

    cart_item_id = request.POST.get("cart_item_id")
    quantity = request.POST.get("quantity")

    if not cart_item_id or not quantity:
        return JsonResponse({
            "success": False,
            "message": "Missing information"
        })

    quantity = int(quantity)

    if quantity < 1:
        return JsonResponse({
            "success": False,
            "message": "Quantity must be at least 1"
        })

    cart_dao = CartDAO()

    cart_dao.update_cart_item_quantity(
        cart_item_id,
        quantity
    )

    return JsonResponse({
        "success": True,
        "message": "Quantity updated"
    })

def remove_from_cart(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Invalid request"
        })

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({
            "success": False,
            "message": "Please login first"
        })

    cart_item_id = request.POST.get("cart_item_id")

    if not cart_item_id:
        return JsonResponse({
            "success": False,
            "message": "Missing cart item"
        })

    cart_dao = CartDAO()

    cart_dao.remove_cart_item(
        cart_item_id
    )

    return JsonResponse({
        "success": True,
        "message": "Item removed from cart"
    })

def check_product_in_cart(request, product_id):

    user_id = request.session.get("user_id")

    if not user_id:
        return JsonResponse({
            "success": True,
            "in_cart": False,
            "quantity": 0
        })

    cart_dao = CartDAO()

    user_cart = cart_dao.get_cart_by_user(user_id)

    if not user_cart:
        return JsonResponse({
            "success": True,
            "in_cart": False,
            "quantity": 0
        })

    cart_item = CartItem.objects.filter(
        cart_id=user_cart.cart_id,
        product_id=product_id
    ).first()

    if cart_item:
        return JsonResponse({
            "success": True,
            "in_cart": True,
            "quantity": cart_item.quantity
        })

    return JsonResponse({
        "success": True,
        "in_cart": False,
        "quantity": 0
    })