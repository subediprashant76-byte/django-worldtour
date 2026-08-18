from django.db import models

# Create your models here.
class Tour(models.Model):
    #we need a origin country,dest,no of nights, price for the tour
    name=models.CharField(max_length=40)
    origin_country=models.CharField(max_length=50)
    dest_country=models.CharField(max_length=50)
    no_of_nights=models.IntegerField()
    price=models.IntegerField()




    #This is a string representation of the tours
    def __str__(self):
        return f"ID:{self.id}: {name} is travelling from {self.origin_country} to {self.dest_country} for {self.no_of_nights} nights and total price of {self.price}"






    