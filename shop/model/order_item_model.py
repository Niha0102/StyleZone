from django.db import models


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=150)
    size_label = models.CharField(max_length=20)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'
        managed = False