from django.shortcuts import render,HttpResponse
# from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.db import models


# def about(request):
#     return render(request, 'home/aboutus.html')  # Adjust path if necessary


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def services(request):
    # return HttpResponse("this is page")
    return render(request,'services.html')

def contact(request):
    # print(request.method)
    if request.method == "POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        Contactn= request.POST.get("phone")
        desc = request.POST.get("textarea")
        contact = Contact(name=name, email=email,phone=Contactn,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "your message  has been sent")
        # return HttpResponse(f"Thank you {name}, we received your message!")
    
    return render(request,'contact.html')
    # return render(request,'contact.html')


# class Contact(models.Model):
#     name = models.CharField(max_length=100)