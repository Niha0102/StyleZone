from abc import ABC, abstractmethod


class UserDAOInterface(ABC):

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass

    @abstractmethod
    def get_user_by_phone(self, phone):
        pass

    @abstractmethod
    def authenticate_user(self, email, password):
        pass

    @abstractmethod
    def save_user(self, user):
        pass

    @abstractmethod
    def update_user(self, user_id, data):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass