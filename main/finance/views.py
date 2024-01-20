from django.shortcuts import render
from .models import Income, Expense, Savings
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse


@login_required
def home(request):
    return render(request, 'finance/home.html', {'title': 'Analytics'})


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
    fields = [ 'expense_incured', 'amount_incured', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('expense-list')
class ExpenseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Expense
    fields = [ 'expense_incured', 'amount_incured', 'date']

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

    def test_func(self):
        savings = self.get_object()
        return self.request.user == savings.user

    success_url = reverse_lazy('expense-list')