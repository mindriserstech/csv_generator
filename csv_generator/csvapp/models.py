from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)

    class Meta:
        db_table = "csv_users"