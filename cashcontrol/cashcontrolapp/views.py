from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, AccountTransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class AccountTransactionsViewSet(viewsets.ViewSet):
    def list(self, request, account_id=None):
        account = get_object_or_404(Account, id=account_id)
        transactions = Transaction.objects.filter(account=account)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)