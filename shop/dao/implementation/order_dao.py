from shop.model.order_model import Order
from shop.model.order_item_model import OrderItem


class OrderDAO:

    # ================================
    # Get All Orders
    # ================================

    @staticmethod
    def get_all_orders():

        return Order.objects.all()


    # ================================
    # Create Order
    # ================================

    @staticmethod
    def create_order(
        user_id,
        total_amount,
        payment_method,
        delivery_address
    ):

        order = Order.objects.create(
            user_id=user_id,
            total_amount=total_amount,
            payment_method=payment_method,
            order_status='Placed',
            delivery_address=delivery_address
        )

        return order


    # ================================
    # Create Order Item
    # ================================

    @staticmethod
    def create_order_item(
        order_id,
        product_id,
        product_name,
        size_label,
        quantity,
        unit_price,
        subtotal
    ):

        order_item = OrderItem.objects.create(
            order_id=order_id,
            product_id=product_id,
            product_name=product_name,
            size_label=size_label,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )

        return order_item