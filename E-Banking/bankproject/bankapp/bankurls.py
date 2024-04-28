# create your urls here...
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name="index"),
    path('createaccount/', views.createaccount, name="createaccount"),
    path('create/', views.create, name="create"),
    path('login/', views.login, name="login"),
    path('logcode/', views.logcode, name="logcode"),
    path('deposite/', views.logcode, name="deposit"),
    path('Successfully_deposit/', views.deposit_final, name="deposit_final"),
    path('withdraw/', views.logcode, name="withdraw"),
    path('withdraw_Successfully/', views.withdraw_final, name="withdraw_final"),
    path('transfer/', views.logcode, name="transfer"),
    path('transfer_final', views.transfer, name="transfer_final")
]