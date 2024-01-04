from django.shortcuts import render
from .models import Income


def home(request):
    return render(request, 'finance/home.html', {'title':'Analytics'})
# Create your views here.
def income(request):
    income_list = Income.objects.all()
    print(income_list)  # Add this line for debugging
    return render(request, 'finance/income.html', {'title': 'Income', 'income_list': income_list})

def expense(request):
    return render(request, 'finance/expense.html',{'title':'expense'})

def savings(request):
    return render(request, 'finance/savings.html',{'title':'happy '})