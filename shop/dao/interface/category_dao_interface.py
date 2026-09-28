from abc import ABC, abstractmethod


class CategoryDAOInterface(ABC):

    @abstractmethod
    def get_all_categories(self):
        pass

    @abstractmethod
    def get_category_by_id(self, category_id):
        pass

    @abstractmethod
    def get_category_by_name(self, category_name):
        pass

    @abstractmethod
    def get_active_categories(self):
        pass

    @abstractmethod
    def save_category(self, category):
        pass

    @abstractmethod
    def update_category(self, category_id, data):
        pass

    @abstractmethod
    def delete_category(self, category_id):
        pass