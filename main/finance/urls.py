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
)

urlpatterns = [
    path('', home, name='home'),
    path('income/', IncomeListView.as_view(), name='income-list'),
    path('income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),
    path('income/create/', IncomeCreateView.as_view(), name='income-create'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),
    path('expense/', expense, name='expense'),
    path('savings/', savings, name='savings'),
]
