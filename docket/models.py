from django.db import models

class Docket(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    no_of_hours_worked = models.IntegerField()
    rate_per_hour = models.FloatField()
    supplier_name = models.CharField(max_length=50)
    po_number = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
