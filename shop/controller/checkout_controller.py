from django.shortcuts import render, redirect

from shop.model.order_model import Order
from shop.model.order_item_model import OrderItem
from shop.model.product_model import Product

from shop.dao.implementation.order_dao import OrderDAO


def checkout(request):

    # Check logged-in user
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')


    # Get user
    from shop.model.user_model import User

    user = User.objects.get(
        user_id=user_id
    )


    # Get cart
    from shop.model.cart_model import Cart
    from shop.model.cart_item_model import CartItem

    cart = Cart.objects.filter(
        user_id=user_id
    ).first()


    if not cart:
        return redirect('cart')


    # Get cart items
    cart_items = CartItem.objects.filter(
        cart_id=cart.cart_id
    )


    if not cart_items.exists():
        return redirect('cart')


    # Prepare checkout items
    checkout_items = []

    total = 0

    for item in cart_items:

        product = Product.objects.get(
            product_id=item.product_id
        )

        subtotal = (
            item.quantity *
            item.unit_price
        )

        checkout_items.append({
            'cart_item': item,
            'product': product,
            'subtotal': subtotal
        })

        total += subtotal


    # ================================
    # Place Order
    # ================================

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        payment_method = request.POST.get('payment_method')


        delivery_address = (
            full_name
            + ', '
            + phone
            + ', '
            + address
            + ', '
            + city
        )


        # Create Order

        order = OrderDAO.create_order(
            user_id=user_id,
            total_amount=total,
            payment_method=payment_method,
            delivery_address=delivery_address
        )


        # Create Order Items

        for item in cart_items:

            product = Product.objects.get(
                product_id=item.product_id
            )

            subtotal = (
                item.quantity *
                item.unit_price
            )

            OrderDAO.create_order_item(
                order_id=order.order_id,
                product_id=product.product_id,
                product_name=product.product_name,
                size_label=item.size_label,
                quantity=item.quantity,
                unit_price=item.unit_price,
                subtotal=subtotal
            )


        # Clear cart

        cart_items.delete()


        # Go to success page

        return redirect(
            'order_success',
            order_id=order.order_id
        )


    return render(
        request,
        'shop/checkout.html',
        {
            'user': user,
            'cart_items': checkout_items,
            'total': total
        }
    )