from django.shortcuts import render
from .models import CustomProduct
# Create your views here.
def index(request):
    products = CustomProduct.objects.all()
    return render(request,'index.html',{'products':products})