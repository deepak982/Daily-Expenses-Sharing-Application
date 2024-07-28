from django.db import models
from django.core.exceptions import ValidationError

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
    participants = models.JSONField(default=dict)  # Expected to be a dict like {'user_id': amount}

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.split_expense()
        super().save(*args, **kwargs)

    def split_expense(self):
        if not self.participants:
            raise ValidationError("Participants must be provided to split the expense.")

        num_participants = len(self.participants)
        if self.split_method == 'equal':
            split_amount = self.total_amount / num_participants
            self.participants = {user_id: split_amount for user_id in self.participants}
        
        elif self.split_method == 'exact':
            total_split = sum(self.participants.values())
            if total_split != self.total_amount:
                raise ValidationError("The sum of exact amounts must equal the total amount.")
        
        elif self.split_method == 'percentage':
            total_percentage = sum(self.participants.values())
            if total_percentage != 100:
                raise ValidationError("The sum of percentages must equal 100.")
            self.participants = {user_id: (self.total_amount * percentage / 100) for user_id, percentage in self.participants.items()}

        else:
            raise ValidationError(f"Unknown split method: {self.split_method}")
