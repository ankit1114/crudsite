from django.db import models
from django.utils import timezone
class Details(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    class Meta:
        db_table = "crudapp"
