from django.db import models


class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    size_label = models.CharField(max_length=20)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart_items'
        managed = False