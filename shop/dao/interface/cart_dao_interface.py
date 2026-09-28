from abc import ABC, abstractmethod


class CartDAOInterface(ABC):

    @abstractmethod
    def get_all_carts(self):
        pass

    @abstractmethod
    def get_cart_by_id(self, cart_id):
        pass

    @abstractmethod
    def get_cart_by_user(self, user_id):
        pass

    @abstractmethod
    def create_cart(self, user_id):
        pass

    @abstractmethod
    def update_cart(self, cart_id, data):
        pass

    @abstractmethod
    def delete_cart(self, cart_id):
        pass