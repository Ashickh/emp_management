from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm

class HomeView(View):
    def get(self,request):
        return render(request,'calc-home.html')

class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        # result=int(n1)+int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1+n2
            # print(form.cleaned_data)
            return render(request,'add.html',{'res':result})
        else:
            return render(request,'sub.html',{'form':form})


class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'sub.html',{'form':form})
    def post(self,request):
        # n1 = request.POST.get ('num1')
        # n2 = request.POST.get ('num2')
        # result = int (n1) - int (n2)
        # print (result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1-n2
            return render (request, 'sub.html', {"subres": result})
        else:
            return render(request,"sub.html",{'form':form})


class MultView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'mult.html',{'form':form})
    def post(self,request):
        # n1 = request.POST.get ('num1')
        # n2 = request.POST.get ('num2')
        # result = int (n1) * int (n2)
        # print (result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1*n2
            return render(request,'mult.html',{"multres":result})
        else:
            return render (request, 'mult.html', {"form":form})

class DivView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'div.html',{'form':form})
    def post(self,request):
        # n1 = request.POST.get ('num1')
        # n2 = request.POST.get ('num2')
        # result = int (n1) / int (n2)
        # print (result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1/n2
            return render(request,"div.html",{"divres":result})
        else:
            return render (request, 'div.html', {"form": form})

class WordcountView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'wordcount.html',{'form':form})
    def post(self,request):
        word=request.POST.get('number')
        words=word.split(" ")
        wc={}
        for w in words:
            if w not in wc:
                wc[w]=0
            wc[w]+=1
        for k,v in wc.items():
            print(k,v)


        return render(request,'wordcount.html',{'wordres':wc})

class PrimeView(View):
    def get(self,request):
        return render(request,'prime.html')
    def post(self,request):
        n1=request.POST.get('num1')
        n2=request.POST.get('num2')
        prime=[]
        for num in range (n1, n2 + 1):
            for i in range (2, num):
                if num % i == 0:
                    break
            else:
                prime.append(num)
        print (prime)
        return render(request,'prime.html',{'result':prime})

# Create your views here.
