from django import forms

class LoginForm(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class RegForm(forms.Form):
    f_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter First Name"}))
    l_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Last Name"}))
    e_mail=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Email"}))
    u_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Username"}))
    pwd=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter password"}))

class EmployeeForm(forms.Form):
    eid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Emp ID"}))
    emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill", "placeholder":"Enter Name"}))
    desig=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Designation"}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Salary"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Email"}))
    experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control rounded-pill","placeholder":"Enter Experience"}))
    def clean(self):
        cleaned_data=super().clean()
        exp=cleaned_data.get("experience")
        if exp<0:
            msg="Invalid Exp"
            self.add_error("experience",msg)

