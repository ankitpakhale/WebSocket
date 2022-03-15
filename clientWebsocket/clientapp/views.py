from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from . models import *
# Create your views here.

def CTest(request):
    return HttpResponse("on clientWebsocket")

def Signup(self):
    if self.POST:
        Name = self.POST['name']
        Email = self.POST['email']
        Password = self.POST['password']
        ConfirmPassword = self.POST['confirmPassword']
        try:
            data=clientuser.objects.filter(email=Email)
            if data:
                msg = 'Email already taken'
                return render(self , 'signup.html',{'msg':msg})
            elif ConfirmPassword == Password:
                v = clientuser()
                v.name = Name
                v.email = Email
                v.password = Password
                v.save()
                return redirect('LOGIN')
            else:
                msg = 'Enter Same Password'
                return render(self , 'signup.html',{'msg':msg})                 
        finally:
            messages.success(self, 'Signup Successfully Done...')

    return render(self,'signup.html')

def Login(self):
    c = ''
    if self.POST:
        em = self.POST.get('email')
        pass1 = self.POST.get('password')
        
        check = clientuser.objects.get(email = em)
        print("Email is ",em,check.email)
        if check.password == pass1:
            self.session['email'] = check.email
            c = 'connect'
            # return redirect('INDEX')
        else:
            return HttpResponse('Invalid Password')
    return render(self,'login.html', {'c' : c})


def Index(self):
    if 'email' in self.session:
        return render(self, 'index.html')
    return redirect('LOGIN')

def ClientLogOut(self):
    del self.session['email']
    print('User logged out')
    return redirect('LOGIN')