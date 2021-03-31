from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request): 
    return render(request,'blog/bloghome.html')

def blogPost(request): 
    return render(request,'blog/blogpost.html')