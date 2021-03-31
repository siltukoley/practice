from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request): 
    return render(request,'home/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact.save()
    return render(request,'home/contact.html')

def about(request): 
    return render(request,'home/about.html')