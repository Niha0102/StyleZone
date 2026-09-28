from abc import ABC, abstractmethod


class OrderDAOInterface(ABC):

    @abstractmethod
    def get_all_orders(self):
        pass

    @abstractmethod
    def get_order_by_id(self, order_id):
        pass

    @abstractmethod
    def get_orders_by_user(self, user_id):
        pass

    @abstractmethod
    def get_orders_by_status(self, order_status):
        pass

    @abstractmethod
    def create_order(self, order):
        pass

    @abstractmethod
    def update_order_status(self, order_id, order_status):
        pass

    @abstractmethod
    def delete_order(self, order_id):
        pass