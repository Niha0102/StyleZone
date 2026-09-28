from shop.model.product_model import Product
from shop.dao.interface.product_dao_interface import ProductDAOInterface


class ProductDAO(ProductDAOInterface):

    def get_all_products(self):
        return Product.objects.all()

    def get_product_by_id(self, product_id):
        return Product.objects.get(product_id=product_id)

    def get_products_by_category(self, category_id):
        return Product.objects.filter(category_id=category_id)

    def get_best_seller_products(self):
        return Product.objects.filter(is_best_seller=True)

    def get_products_by_brand(self, brand):
        return Product.objects.filter(brand=brand)

    def get_products_by_color(self, color):
        return Product.objects.filter(color=color)

    def get_products_by_price_range(self, min_price, max_price):
        return Product.objects.filter(
            price__gte=min_price,
            price__lte=max_price
        )

    def search_products(self, keyword):
        return Product.objects.filter(
            product_name__icontains=keyword
        )

    def get_active_products(self):
        return Product.objects.filter(is_active=True)

    def save_product(self, product):
        product.save()
        return product

    def update_product(self, product_id, data):
        Product.objects.filter(
            product_id=product_id
        ).update(**data)

        return Product.objects.get(product_id=product_id)

    def delete_product(self, product_id):
        return Product.objects.filter(
            product_id=product_id
        ).delete()