from shop.model.category_model import Category


class CategoryDAO:

    @staticmethod
    def get_all_categories():
        return Category.objects.all()