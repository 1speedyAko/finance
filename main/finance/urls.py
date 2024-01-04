from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('income/', views.income , name='income'),
    path('expense/', views.expense , name = 'expense'),
    path('savings/', views.savings , name = 'savings')
]