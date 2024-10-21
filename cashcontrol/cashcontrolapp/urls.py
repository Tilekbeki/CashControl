from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, TransactionViewSet, AccountTransactionsViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('accounts/<int:account_id>/transactions/', AccountTransactionsViewSet.as_view({'get': 'list'}), name='account-transactions'),
    ]
