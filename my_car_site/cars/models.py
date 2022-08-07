from django.db import models

# Create your models here.
class Car(models.Model):
    # primary key automated
    brand = models.CharField(max_length=30, default="automobiili")
    year = models.IntegerField(default=1988)

    def __str__(self):
        return f"Car ID {self.pk} is {self.brand} {self.year}"