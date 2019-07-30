from django.db import models
from django.utils import timezone
class Details(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    email = models.emailfield(max_length=100)
    contact = models.IntegerField(max_length=25)
    class Meta:
        db_table = "details"
