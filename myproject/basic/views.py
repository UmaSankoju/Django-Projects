from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactus(request):
    return render(request, 'contactus.html')

def sample1(request):
    qp1 = request.GET.get("name")
    return HttpResponse(f"Hello {qp1}  welcome to the website")

def sample(request):
    info = {"data":[{"name": "uma", "city":"hyd", "gender":"female"},{"name": "rishi", "city":"chennai", "gender":"male"},{"name": "harsha", "city":"banglore", "gender":"male"}]}
    return JsonResponse(info)