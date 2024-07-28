   
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=True, methods=['get'])
    def user_expenses(self, request, pk=None):
        expenses = Expense.objects.filter(user_id=pk)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='all_expenses')
    def all_expenses(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
