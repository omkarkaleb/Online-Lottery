from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from itertools import chain
from django.utils.translation import gettext as _
from django.contrib.auth.models import User, auth
from django.views.generic import TemplateView
from django.contrib import messages

def loginregister(request):
    return render(request, 'loginregister.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:

        
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, 'Already Registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username, email= email, password=password)
                return redirect('loginregister')   

        else:
            messages.info(request, 'Passwords dont match')
            return redirect('register')            
           
    else:
        return render(request, 'register.html')   
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Wrong Credentials YOU IDIOT!!!')
            return redirect('login')
    else:
        return render(request, 'login.html')   
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def viewresult(request):
    one = int('0' + request.POST.get('1'))
    two = int('0' + request.POST.get('2'))
    three = int('0' + request.POST.get('3'))
    four = int('0' + request.POST.get('4'))
    five = int('0' + request.POST.get('5'))
    six = int('0' + request.POST.get('6'))
    seven = int('0' + request.POST.get('7'))
    eight = int('0' + request.POST.get('8'))
    nine = int('0' + request.POST.get('9'))
    ten = int('0' + request.POST.get('10'))

    lis = []
    lis1 = []
    lis.extend((one, two, three, four, five, six, seven, eight, nine, ten))

    summ = one + two + three + four + five + six + seven + eight + nine + ten
    print(summ)

    summm = summ * 0.7
    divident = summm/10

    for i in lis:
        if i < divident:
            lis1.append((i))

    lis1.sort(reverse=True)
    result = lis1[0]

    if one == result:
        rr = 1
    elif two == result:
        rr = 2   
    elif three == result:
        rr = 3
    elif four == result:
        rr = 4
    elif five == result:
        rr = 5 
    elif six == result:
        rr = 6 
    elif seven == result:
        rr = 7 
    elif eight == result:
        rr = 8 
    elif nine == result:
        rr = 9 
    elif ten == result:
        rr = 10 

    return render(request, 'result.html', {'rr': rr})
