from django.db import models


class Cart(models.Model):

    cart_id = models.AutoField(primary_key=True)

    user_id = models.IntegerField(
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = 'cart'

        managed = False