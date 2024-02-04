from django.shortcuts import render
from django.shortcuts import  HttpResponse,Http404,get_object_or_404
from .models import *
# Create your views here.

def home(request):
    pets=Pet.objects.all()
    return render(request,"home.html",{'pets':pets,})

def pet_detail(request,pet_id):
    pet=get_object_or_404(Pet,id=pet_id)
  
    return render(request,"pet_detial.html",{'pet':pet,})