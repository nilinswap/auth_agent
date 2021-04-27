from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "user"

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    dob = models.CharField(max_length=50)
