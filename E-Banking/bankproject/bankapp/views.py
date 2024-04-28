from django.shortcuts import render
from . models import Account
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def createaccount(request):
    return render(request, "createaccount.html")

def create(request):
    acno = ''
    for x in range(6):
        acno = acno + str(randint(0,9))
    acno = int(acno)
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['address']
    contactNO = request.POST['number']
    emailAddress = request.POST['email']
    panNO = request.POST['panno']
    adharNO = request.POST['adharno']
    balance = request.POST['balance']
    password = request.POST['password']

    ac = Account(acno=acno, name=name, gender=gender, address=address, contactno=contactNO, emailaddress=emailAddress, panno=panNO, adharno=adharNO, balance=balance, password=password)
    ac.save()
    msg = 'Your account no is: '+ str(acno)
    return render(request, "create.html", {'msg': msg})

def login(request):
    return render(request, "login.html")

def logcode(request):
    acno = request.POST['acno']
    password = request.POST['password']
    operation = request.POST['operation']
    msg = ''
    try:
        obj = Account.objects.get(acno = acno, password = password)
        if operation == "Deposit":
            acno = obj.acno
            request.session['acno'] = acno
            return render(request, "deposit.html")
        elif operation == "Withdraw":
            acno = obj.acno
            request.session['acno'] = acno
            return render(request, "withdraw.html")
        elif operation == "Transfer":
            acno = obj.acno
            request.session['acno'] = acno
            return render(request, "transfer.html")
        elif operation == "Enquiry":
            balance = obj.balance
            return render(request, "Enquiry.html", {'msg':balance})
    except ObjectDoesNotExist:
        msg = 'Invalid User...'
        return HttpResponse("Invalid user...")

def deposit_final(request):
    amount = int(request.POST['amount'])
    obj = Account.objects.get(acno = request.session['acno'])
    balance = obj.balance
    balance = balance + amount
    acno = obj.acno
    Account.objects.filter(pk=acno).update(balance=balance)
    request.session['acno'] = None
    msg = 'Amount is Credited!'
    return render(request, "deposit_final.html", {"msg":msg})

def withdraw_final(request):
    amount = int(request.POST['amount'])
    obj = Account.objects.get(acno = request.session['acno'])
    balance = obj.balance
    balance = balance - amount
    acno = obj.acno
    msg = ''
    if balance < amount:
        msg = msg + 'Insufficient balance'
        return render(request, "Error.html", {"msg": msg})
    balance = balance-amount
    Account.objects.filter(pk=acno).update(balance=balance)
    msg = msg + 'Amount is debited!'
    request.session['acno'] = None
    return render(request, "withdraw_final.html", {"msg":msg})

def transfer(request):
    b_acno = int(request.POST['b_acno']) #beneficiary account number
    amount = int(request.POST['amount']) # amount to be transferred
    obj1 = Account.objects.get(acno = request.session['acno'])
    msg = ''

    try:
        obj2 = Account.objects.get(acno = b_acno)
        acno1 = obj1.acno  # acno of person who will transafer
        acno2 = obj2.acno  # acno of person who wll recieve
        balance1 = obj1.balance
        balance2 = obj2.balance
        if balance1 < amount:
            msg = msg + 'Insufficient balance'
            request.session['acno'] = None
            return render(request, "Error.html", {"msg": msg})
        balance1 = balance1 - amount
        balance2 = balance2 + amount

        Account.objects.filter(pk=acno1).update(balance=balance1)
        Account.objects.filter(pk=acno2).update(balance=balance2)
        msg = msg + 'Amount is Trnsferred...'
        request.session['acno'] = None
        return render(request, "transfer_final.html", {'msg':msg})
    except ObjectDoesNotExist:
        msg = msg + 'Beneficiary Account does not exist!'
        return render(request, "Error.html", {'msg':msg})