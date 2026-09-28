from django.shortcuts import render, redirect

from shop.model.order_model import Order


def my_orders(request):

    user_id = request.session.get('user_id')
    print("CURRENT USER ID:", user_id)
    
    if not user_id:
        return redirect('login')

    orders = Order.objects.filter(
        user_id=user_id
    ).order_by('-order_id')

    return render(
        request,
        'shop/my_orders.html',
        {
            'orders': orders
        }
    )