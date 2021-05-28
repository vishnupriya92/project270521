from django.shortcuts import render

# Create your views here.
name="vishnupriya"
email="vishnupriya413@gmail.com"
phno=9741576925
def index(request):
    return render(request,"home.html",{'name':name})

def menu(request):
    return render(request,"menu.html",{'name':name})

def details(request):
    return render(request,"contact.html",{"name":name,"email":email,"phno":phno})