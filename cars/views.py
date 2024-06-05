from django.shortcuts import render
from .models import Car, Owner, Rentacar

# Create your views here.

def general__view(request):
    cars = Car.objects.all()
    owners = Owner.objects.all()
    rentacars = Rentacar.objects.all()
    
    context = {
        "cars": cars,
        "owners": owners,
        "rentacars": rentacars
    }
    
    return render(request, 'index.html', context)
