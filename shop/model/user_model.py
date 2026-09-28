from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'
        managed = False