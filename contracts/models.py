from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField(auto_now_add=False)
    def __str__(self):
        return self.description