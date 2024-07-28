
from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    SPLIT_METHODS = [
        ('equal', 'Equal'),
        ('exact', 'Exact'),
        ('percentage', 'Percentage')
    ]

    description = models.CharField(max_length=255)
    total_amount = models.FloatField()
    split_method = models.CharField(max_length=10, choices=SPLIT_METHODS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    participants = models.JSONField(default=dict)

    def __str__(self):
        return self.description
