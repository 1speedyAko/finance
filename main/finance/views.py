from django.shortcuts import render
from django.views import View
from .models import Income, Expense, Savings
from django.http import JsonResponse
from collections import defaultdict
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
import json



@login_required
def home(request):
    category_summaries = Income.objects.values('category').annotate(total_amount=Sum('amount'))


    label_amount_map = defaultdict(int)  # Using defaultdict to initialize unknown keys with 0
    queryset = Expense.objects.all()  # Fetch all expenses
    for expense in queryset:
        label_amount_map[expense.expense_incured] += expense.amount  # Accumulate amounts for each label

    labels = list(label_amount_map.keys())  # Get the labels
    data = list(label_amount_map.values())  # Get the accumulated amounts



    return render(request, 'finance/home.html', {
        'labels': labels,
        'data': data,
        'category_summaries': category_summaries,

    })

class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'finance/income.html'
    context_object_name = 'income_list'
    ordering = ['-date_joined']


class IncomeDetailView(LoginRequiredMixin, DetailView):
    model = Income


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    fields = [ 'category', 'amount', 'date_joined']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('income-list')

class IncomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    fields = ['category', 'amount', 'date_joined']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.user


class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    success_url = reverse_lazy('home')

    def test_func(self):
        income = self.get_object()
        return self.request.user == income.user


@login_required
def expense(request):
    return render(request, 'finance/expense.html', {'title': 'expense'})

class ExpenseListView(LoginRequiredMixin,ListView):
    model = Expense
    template_name = 'finance/expense.html'
    context_object_name = 'expense_list'
    ordering = ['-date']

    

class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    fields = [ 'expense_incured', 'amount', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('expense-list')
class ExpenseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Expense
    fields = [ 'expense_incured', 'amount', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        expense = self.get_object()
        return self.request.user == expense.user

class ExpenseDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = Expense

    def test_func(self):
        expense = self.get_object()
        return self.request.user == expense.user

    success_url = reverse_lazy('expense-list')

@login_required
def savings(request):
    return render(request, 'finance/savings.html', {'title': 'happy'})

class SavingListView(LoginRequiredMixin, ListView):
    model = Savings
    template_name = 'finance/savings.html'
    context_object_name = 'savings_list'
    ordering = ['-date_saved']
     
class SavingDetailView(LoginRequiredMixin,DetailView):
    model = Savings

class SavingCreateView(LoginRequiredMixin, CreateView):
    model = Savings
    fields = [ 'goal', 'target_amount', 'amount_saved', 'date_saved']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('saving-list')

class SavingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Savings
    fields = [ 'goal', 'target_amount', 'amount_saved', 'date_saved']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        saving = self.get_object()
        return self.request.user == saving.user

class SavingDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = Savings
    # success_url = 'saving-list'

    def test_func(self):
        savings = self.get_object()
        return self.request.user == savings.user

    success_url = reverse_lazy('saving-list')
