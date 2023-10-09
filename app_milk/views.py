from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def feature(request):
    return render(request,'feature.html')

def gallery(request):
    return render(request,'gallery.html') 

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')