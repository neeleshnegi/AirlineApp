from django.shortcuts import render

from .models import flight

# Create your views here.

def index(request):
    return render(request, 'flights/index.html',{'flights': flight.objects.all()})


def Flight(request, flight_id):
    Flight = flight.objects.get(pk=flight_id)
    return render(request,'flights/flight.html',{'flight' : Flight})


