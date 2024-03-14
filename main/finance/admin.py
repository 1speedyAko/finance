from django.contrib import admin
# from django_admin_charts.models import Chart
from .models import *
# Register your models here.
# class IncomeAdmin(admin.ModelAdmin):
#     list_display = ( 'category', 'amount')
#     chart_views = [
#         Chart(
#             title='Income by Category',
#             chart_type='pie',
#             model=Income,
#             filter_field='category',
#             colors=[
#                 '#FF5733',  # Dog Training
#                 '#33FF57',  # Dog Sales
#                 '#3366FF',  # Equipment Sales
#                 '#FF33FF',  # Kitchen
#                 '#FFFF33',  # Donations
#             ],
#             group_by='category',
#             sum_by='amount',
#         ),
#     ]

admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Savings)
admin.site.register(Expense)