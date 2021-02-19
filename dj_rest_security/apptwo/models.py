from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    state = models.CharField(max_length=30)

    class Meta:
        db_table = 'ADR_INFO'