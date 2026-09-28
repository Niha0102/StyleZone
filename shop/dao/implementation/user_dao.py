from shop.model.user_model import User


class UserDAO:

    @staticmethod
    def get_all_users():
        return User.objects.all()