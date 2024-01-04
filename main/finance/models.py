from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    DOG_TRAINING = 'DT'
    DOG_SALES = 'DS'
    EQUIPMENT_SALES = 'EQ'
    KITCHEN = 'KT'
    DONATIONS = 'DN'
    
    SELECTION_CHOICES = [
        (DOG_TRAINING, 'Dog Training'),
        (DOG_SALES, 'Dog Sales'),
        (EQUIPMENT_SALES, 'Equipment Sales'),
        (KITCHEN, 'Kitchen'),
        (DONATIONS, 'Donations')
    ]
    
    user_selection = models.CharField(max_length=2, choices=SELECTION_CHOICES, default=DOG_TRAINING)

    def __str__(self):
        return f"{self.get_user_selection_display()} - {self.user}" 

class Income(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=Category.SELECTION_CHOICES , default = 0)
    amount = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" posted by {self.user}  is {self.amount}"
    
class Savings(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal = models.CharField(max_length=30, blank=False)
    target_amount = models.IntegerField(blank=False, default=0)
    amount_saved = models.DecimalField(max_digits=10 , decimal_places=2, blank=False, default=0)
    date_saved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

    # def save(self, *args, **kwargs):
    #     super(Savings,self).save(*args, **kwargs)
    

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    expense_incured = models.CharField(max_length = 30, blank=False, default=0)
    amount_incured = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


    def __str__(self):
        return str(self.user)