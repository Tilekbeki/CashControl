from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, AccountTransactionSerializer
import datetime


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class AccountTransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        account_id = kwargs.get('account_id')
        transactions = Transaction.objects.filter(account_id=account_id)
        serialized_transactions = self.get_serializer(transactions, many=True).data
        new_array = [{}]

        for transaction in serialized_transactions:
            timestamp = transaction['timestamp']
            try:
                string_as_date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                string_as_date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
            
            day = string_as_date.day
            if day not in new_array:
                new_array[0][day] = []
            
            new_array[0][day].append(transaction)

        return Response(serialized_transactions)