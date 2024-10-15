from django.db import models

# Create your models here.
class Account(models.Model):
    TRANSACTION_TYPES = [
        ('dollar', 'Dollar'),
        ('rub', 'Rub'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    currency = models.CharField(max_length=30, choices=TRANSACTION_TYPES)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.account.name}"