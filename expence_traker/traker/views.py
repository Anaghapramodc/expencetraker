from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Expense
from .serializers import ExpenseSerializer, categorySerializer
import datetime
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.db.models import Q


class categoryCreateView(APIView):
    def post(self, request, format=None):
        serializer = categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "category added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseCreateView(APIView):
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Expense added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseListView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseEditAPIView(generics.RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Expense updated successfully.', 'data': serializer.data})

    def perform_update(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class ExpenseDeleteView(APIView):
    def delete(self, request, expense_id):
        expense = get_object_or_404(Expense, pk=expense_id)
        expense.delete()
        message = {'detail': 'Expense successfully deleted.'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)




class searchView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'category__name']  # Update this line
