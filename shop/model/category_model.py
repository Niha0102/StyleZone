from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categories'
        managed = False