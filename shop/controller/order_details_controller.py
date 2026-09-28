from django.shortcuts import render, redirect

from shop.model.order_model import Order
from shop.model.order_item_model import OrderItem


def order_details(request, order_id):

    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    order = Order.objects.filter(
        order_id=order_id,
        user_id=user_id
    ).first()

    if not order:
        return redirect('my_orders')

    order_items = OrderItem.objects.filter(
        order_id=order_id
    )

    return render(
        request,
        'shop/order_details.html',
        {
            'order': order,
            'order_items': order_items
        }
    )