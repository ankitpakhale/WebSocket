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
        print(Name)
        Email = self.POST['email']
        print(Email)
        Password = self.POST['password']
        print(Password)
        ConfirmPassword = self.POST['confirmPassword']
        print(ConfirmPassword)

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
    if self.POST:
        em = self.POST.get('email')
        pass1 = self.POST.get('password')
        try:
            check = clientuser.objects.get(email = em)
            print("Email is ",em,check.email)
            if check.password == pass1:
                # print(check.Password)
                self.session['email'] = check.email
                return redirect('INDEX')
                # nameMsg = CasignUp.objects.get(email = em)
                # msg = 'User Successfully logged in'
                # print(msg)
                # return render(self, 'dashboard.html', {'key':nameMsg})
            else:
                return HttpResponse('Invalid Password')
        except:
            print("Inside first except block")
            return HttpResponse('Invalid Email ID')
    return render(self,'login.html')

def Index(self):
    if 'email' in self.session:
        return render(self, 'index.html')
    return redirect('LOGIN')

def ClientLogOut(self):
    del self.session['email']
    print('User logged out')
    return redirect('LOGIN')