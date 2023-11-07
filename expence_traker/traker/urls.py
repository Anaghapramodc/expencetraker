
from django.urls import path
from .views import ExpenseCreateView, categoryCreateView, ExpenseListView, ExpenseDetailView, ExpenseEditAPIView, \
    ExpenseDeleteView, searchView

urlpatterns = [
    path('category/', categoryCreateView.as_view(), name='category-create'),
    path('expenses/', ExpenseCreateView.as_view(), name='expense-create'),
    path('expenses_list/', ExpenseListView.as_view(), name='expense-list'),
    path('expenses_detaildview/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expenses-update/<int:pk>/', ExpenseEditAPIView.as_view(), name='edit-expense'),
    path('expenses-delete/<int:expense_id>/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('expenses-search/', searchView.as_view(), name='expense-search'),

]



