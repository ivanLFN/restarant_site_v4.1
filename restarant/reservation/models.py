import datetime
from django.db import models

class Table(models.Model):
    name_table = models.CharField(max_length=10)
    state = models.BooleanField(default=True)
    count_person = models.IntegerField()

    def __str__(self) -> str:
        return self.name_table
    

class ReservationTable(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    date_time = models.DateTimeField(default=datetime.datetime.now)
    count_person = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    