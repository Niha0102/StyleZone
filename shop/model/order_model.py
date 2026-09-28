from django.db import models


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    order_status = models.CharField(max_length=30, default='Placed')
    delivery_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'orders'
        managed = False