from django.shortcuts import render
from .models import Income
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


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
    fields = ['user', 'category', 'amount', 'date_joined']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    fields = ['user', 'category', 'amount', 'date_joined']

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


@login_required
def savings(request):
    return render(request, 'finance/savings.html', {'title': 'happy'})
