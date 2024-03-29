from django.urls import path
from .views import (
    home,
    IncomeListView,
    IncomeDetailView,
    IncomeCreateView,
    IncomeUpdateView,
    IncomeDeleteView,
    expense,
    savings,
    ExpenseListView,
    ExpenseDetailView,
    ExpenseCreateView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    SavingListView,
    SavingDetailView,
    SavingCreateView,
    SavingUpdateView,
    SavingDeleteView,
)

urlpatterns = [
    path('', home, name='home'),
    path('income/', IncomeListView.as_view(), name='income-list'),
    path('income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),
    path('income/create/', IncomeCreateView.as_view(), name='income-create'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),
    path('expense/',ExpenseListView.as_view(), name='expense-list'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('expense/<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/',  ExpenseDeleteView.as_view(), name='expense-delete'),
    path('savings/', SavingListView.as_view(), name='saving-list'),
    path('savings/<int:pk>/', SavingDetailView.as_view(), name = 'saving-detail' ),
    path('savings/create/', SavingCreateView.as_view(), name='saving-create'),
    path('savings/<int:pk>/update/', SavingUpdateView.as_view(), name='saving-update'),
    path('savings/<int:pk>/delete/',  SavingDeleteView.as_view(), name='saving-delete'),

]