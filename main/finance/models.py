from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    DOG_TRAINING = 'Dog Training'
    DOG_SALES = 'Dog Sales'
    EQUIPMENT_SALES = 'Equipment Sales'
    KITCHEN = 'Kitchen'
    DONATIONS = 'Donnations'
    Fresh_Juice = 'Fresh Juice'
    
    SELECTION_CHOICES = [
        (DOG_TRAINING, 'Dog Training'),
        (DOG_SALES, 'Dog Sales'),
        (EQUIPMENT_SALES, 'Equipment Sales'),
        (KITCHEN, 'Kitchen'),
        (DONATIONS, 'Donations'),
        (Fresh_Juice, 'Fresh Juice')

    ]
    
    user_selection = models.CharField(max_length=22, choices=SELECTION_CHOICES, default=DOG_TRAINING)

    def __str__(self):
        return f"{self.get_user_selection_display()} - {self.user}" 

  
class Income(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=22, choices=Category.SELECTION_CHOICES , default = 0)
    amount = models.IntegerField()
    comment = models.CharField(max_length=30 , default='' )
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" posted by {self.user}  is {self.amount}"
    
    def get_absolute_url(self):
        return reverse('income-list' )

class Savings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal = models.CharField(max_length=30, blank=False)
    target_amount = models.IntegerField(blank=False, default=0)
    amount_saved = models.IntegerField()
    date_saved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('saving-list')

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    expense_incured = models.CharField(max_length = 30, blank=False)
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('expense-list')