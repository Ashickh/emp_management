from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# function based requests

# def index(request):
#     return render(request,'home.html')
#
# def login(request):
#     return render(request,'login.html')
#
# def register(request):
#     return HttpResponse('<h1> This is Registration Page</h1>')

# Create your views here.

# class based views

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

class RegView(View):
    def get(self,request):
        return render(request,'reg.html')
    def post(self,request):
        print(request.POST.get('f_name'))
        print(request.POST.get('l_name'))
        print(request.POST.get('e_mail'))
        print(request.POST.get('u_name'))
        print (request.POST.get ('pwd'))
        return render(request,'reg.html')