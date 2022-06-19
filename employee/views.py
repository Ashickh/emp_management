# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.views.generic import View
#
# from employee.forms import EmployeeForm
# from django.contrib import messages
# from employee.forms import LoginForm
# from employee.forms import RegForm


# # Create your views here.
#
# # class based views
#
# class HomeView(View):
#     def get(self,request):
#         return render(request,'home.html')
#
# class LoginView(View):
#     form_class=LoginForm
#     template_name="login.html"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("user_name"))
#             print(form.cleaned_data.get("password"))
#             return render(request,self.template_name,{'form':form})
#         else:
#             return render(request,self.template_name,{'form':form})
#
#
#
#
#
# class RegView(View):
#     form_class=RegForm
#     template_name="reg.html"
#     def get(self,request):
#         form=self.form_class()
#         return render (request, self.template_name, {'form': form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("f_name"))
#             print(form.cleaned_data.get("l_name"))
#             print (form.cleaned_data.get ("e_mail"))
#             print (form.cleaned_data.get ("u_name"))
#             print (form.cleaned_data.get ("pwd"))
#             return render(request,self.template_name,{"form":form})
#         else:
#             return render(request,self.template_name,{"form":form})

from django.shortcuts import render,redirect
from employee.models import Employee
from django.contrib import messages
from django.views.generic import View
from employee.forms import EmployeeCreateForm


class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeCreateForm()
        return render(request,"emp-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST)
        if form.is_valid():
            Employee.objects.create(
                eid=form.cleaned_data.get("eid"),
                emp_name=form.cleaned_data.get("emp_name"),
                desig=form.cleaned_data.get("desig"),
                salary=form.cleaned_data.get("salary"),
                email=form.cleaned_data.get("email"),
                experience=form.cleaned_data.get("experience"),

                )
            messages.success (request, "Employee Added Sccessfully")
            return redirect('emp-add')
        else:
            messages.error(request,"Employee Added Failed")
            return render(request,"emp-add.html",{"form":form})

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        ab=Employee.objects.all()
        return render(request,"emp-list.html",{'employees':ab})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        ab=Employee.objects.get(eid=kwargs.get('emp_id'))
        return render(request,"emp-detail.html",{'employee':ab})