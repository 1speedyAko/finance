from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from users.models import CustomUser
from finance.models import Category, Income, Savings, Expense


class FinanceModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="test_user",
            email="test@example.com",
            password="password123"
        )

    def test_category_creation(self):
        """Test creation of a category"""
        category = Category.objects.create(user=self.user, user_selection=Category.DOG_TRAINING)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(category.user_selection, Category.DOG_TRAINING)
        self.assertEqual(str(category), "Dog Training - test_user")

    def test_income_creation(self):
        """Test creation of an income entry"""
        income = Income.objects.create(user=self.user, category=Category.DOG_TRAINING, amount=100)
        self.assertEqual(Income.objects.count(), 1)
        self.assertEqual(income.category, Category.DOG_TRAINING)
        self.assertEqual(income.amount, 100)
        self.assertEqual(str(income), " posted by test_user  is 100")  # Remove extra space

    def test_savings_creation(self):
        """Test creation of a savings entry"""
        savings = Savings.objects.create(user=self.user, goal="Test Goal", target_amount=1000, amount_saved=500)
        self.assertEqual(Savings.objects.count(), 1)
        self.assertEqual(savings.goal, "Test Goal")
        self.assertEqual(savings.target_amount, 1000)
        self.assertEqual(savings.amount_saved, 500)
        self.assertEqual(str(savings), "test_user")

    def test_expense_creation(self):
        """Test creation of an expense entry"""
        expense = Expense.objects.create(user=self.user, expense_incured="Test Expense", amount_incured=50)
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(expense.expense_incured, "Test Expense")
        self.assertEqual(expense.amount_incured, 50)
        self.assertEqual(str(expense), "test_user")

    def test_income_absolute_url(self):
        """Test absolute URL for Income model"""
        income = Income.objects.create(user=self.user, category=Category.DOG_TRAINING, amount=100)
        expected_url = reverse('income-list')  # Correct view name here
        self.assertEqual(income.get_absolute_url(), expected_url)

    def test_savings_absolute_url(self):
        """Test absolute URL for Savings model"""
        savings = Savings.objects.create(user=self.user, goal="Test Goal", target_amount=1000, amount_saved=500)
        expected_url = reverse('saving-list')  # Correct view name here
        self.assertEqual(savings.get_absolute_url(), expected_url)

    def test_expense_absolute_url(self):
        """Test absolute URL for Expense model"""
        expense = Expense.objects.create(user=self.user, expense_incured="Test Expense", amount_incured=50)
        expected_url = reverse('expense-list')  # Correct view name here
        self.assertEqual(expense.get_absolute_url(), expected_url)
