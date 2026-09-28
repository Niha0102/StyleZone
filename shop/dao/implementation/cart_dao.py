from shop.model.cart_model import Cart
from shop.model.cart_item_model import CartItem


class CartDAO:

    @staticmethod
    def get_all_carts():
        return Cart.objects.all()

    @staticmethod
    def get_cart_by_user(user_id):
        return Cart.objects.filter(user_id=user_id).first()

    @staticmethod
    def create_cart(user_id):
        return Cart.objects.create(user_id=user_id)

    @staticmethod
    def get_cart_items(cart_id):
        return CartItem.objects.filter(cart_id=cart_id)

    @staticmethod
    def add_cart_item(
        cart_id,
        product_id,
        size_label,
        quantity,
        unit_price
    ):
        return CartItem.objects.create(
            cart_id=cart_id,
            product_id=product_id,
            size_label=size_label,
            quantity=quantity,
            unit_price=unit_price
        )

    @staticmethod
    def add_or_update_cart_item(
        cart_id,
        product_id,
        size_label,
        quantity,
        unit_price
    ):

        cart_item = CartItem.objects.filter(
            cart_id=cart_id,
            product_id=product_id,
            size_label=size_label
        ).first()

        if cart_item:

            cart_item.quantity += quantity

            CartItem.objects.filter(
                cart_item_id=cart_item.cart_item_id
            ).update(
                quantity=cart_item.quantity
            )

            return cart_item

        return CartItem.objects.create(
            cart_id=cart_id,
            product_id=product_id,
            size_label=size_label,
            quantity=quantity,
            unit_price=unit_price
        )

    @staticmethod
    def update_cart_item_quantity(cart_item_id, quantity):

        CartItem.objects.filter(
            cart_item_id=cart_item_id
        ).update(
            quantity=quantity
        )



    @staticmethod
    def remove_cart_item(cart_item_id):

        CartItem.objects.filter(
            cart_item_id=cart_item_id
        ).delete()