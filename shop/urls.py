from django.urls import path

from .controller.home_controller import home
from .controller.product_controller import product_list, product_details
from .controller.cart_controller import (
    add_to_cart,
    cart,
    update_cart_quantity,
    remove_from_cart,
    check_product_in_cart
)

from .controller.login_controller import login
from .controller.register_controller import register
from .controller.profile_controller import profile, logout
from shop.controller.checkout_controller import checkout
from shop.controller.order_success_controller import order_success
from shop.controller.my_orders_controller import my_orders
from shop.controller.order_details_controller import order_details

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'products/',
        product_list,
        name='product_list'
    ),

    path(
        'products/<int:product_id>/',
        product_details,
        name='product_details'
    ),

    path(
        'cart/add/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        cart,
        name='cart'
    ),

    path(
        'cart/update-quantity/',
        update_cart_quantity,
        name='update_cart_quantity'
    ),

    path(
    'cart/remove/',
    remove_from_cart,
    name='remove_from_cart'
    ),

    path(
        'login/',
        login,
        name='login'
    ),

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'profile/', 
        profile, 
        name='profile'),

    path('logout/',
         logout, 
         name='logout'),

    path('checkout/',
        checkout,
        name='checkout'),

    path('order-success/<int:order_id>/',
        order_success,
        name='order_success'),

    path('my-orders/',
        my_orders,
        name='my_orders'),

    path('my-orders/<int:order_id>/',
        order_details,
        name='order_details'),

    path(
    'cart/check/<int:product_id>/',
        check_product_in_cart,
        name='check_product_in_cart'),
]