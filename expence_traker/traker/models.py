# models.py
from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Expense(models.Model):
    expense_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Set default date to current date if not provided
        if not self.date:
            self.date = datetime.date.today()
        super().save(*args, **kwargs)
