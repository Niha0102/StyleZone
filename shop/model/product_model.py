from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    product_name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    base_color = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    image_url = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_best_seller = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'
        managed = False