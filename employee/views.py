from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from employee.forms import LoginForm
from employee.forms import RegForm
from employee.forms import EmployeeForm

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

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class LoginView(View):
    form_class=LoginForm
    template_name="login.html"
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("user_name"))
            print(form.cleaned_data.get("password"))
            return render(request,self.template_name,{'form':form})
        else:
            return render(request,self.template_name,{'form':form})





class RegView(View):
    form_class=RegForm
    template_name="reg.html"
    def get(self,request):
        form=self.form_class()
        return render (request, self.template_name, {'form': form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("f_name"))
            print(form.cleaned_data.get("l_name"))
            print (form.cleaned_data.get ("e_mail"))
            print (form.cleaned_data.get ("u_name"))
            print (form.cleaned_data.get ("pwd"))
            return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})




class EmpCreateView(View):
    form_class=EmployeeForm
    template_name="emp-add.html"
    success_temp="add_success.html"
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("eid"))
            print(form.cleaned_data.get("emp_name"))
            print(form.cleaned_data.get("desig"))
            print(form.cleaned_data.get("salary"))
            print (form.cleaned_data.get ("email"))
            print (form.cleaned_data.get ("experience"))
            return render(request,self.success_temp,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})

