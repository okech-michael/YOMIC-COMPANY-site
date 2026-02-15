# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def company(request):
     return render(request, 'core/company.html')
 
def pricing(request):
     return render(request, 'core/pricing.html')    
 
def solutions(request):
     return render(request, 'core/solutions.html')
 
def contact(request):
     return render(request, 'core/contact.html')
 
 



