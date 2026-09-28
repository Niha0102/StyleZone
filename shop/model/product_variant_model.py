from django.db import models


class ProductVariant(models.Model):
    product_size_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    size_label = models.CharField(max_length=20)
    stock_quantity = models.IntegerField(default=0)
    sku_code = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_variants'
        managed = False