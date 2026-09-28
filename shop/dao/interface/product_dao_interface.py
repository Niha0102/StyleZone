from abc import ABC, abstractmethod


class ProductDAOInterface(ABC):

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_products_by_category(self, category_id):
        pass

    @abstractmethod
    def get_products_by_brand(self, brand):
        pass

    @abstractmethod
    def get_products_by_color(self, color):
        pass

    @abstractmethod
    def get_products_by_price_range(self, min_price, max_price):
        pass

    @abstractmethod
    def search_products(self, keyword):
        pass

    @abstractmethod
    def get_active_products(self):
        pass

    @abstractmethod
    def save_product(self, product):
        pass

    @abstractmethod
    def update_product(self, product_id, data):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass