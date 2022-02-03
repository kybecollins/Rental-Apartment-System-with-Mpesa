from django.shortcuts import render

# Create your views here.
def default_home_view(request):
    context={}
    return render(request,'officials/index.html',context)

def default_apartment_view(request):
    context={}
    return render(request,'officials/apartments.html',context)

def default_about_view(request):
    context={}
    return render(request,'officials/about.html',context)

def default_contact_view(request):
    context={}
    return render(request,'officials/contact.html',context)