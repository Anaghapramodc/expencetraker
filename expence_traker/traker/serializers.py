from rest_framework import serializers
from .models import Expense, Category


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)  # Note the comma after 'name'



class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'expense_name', 'amount', 'date', 'category')

