from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Plant
from .forms import PlantForm

# Create your views here.
def index(request):
    plants = Plant.objects.all()
    form = PlantForm()
    return render(request, 'index.html', {'plants' : plants, 'form' : form})

def show(request, auto_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'show.html', {'plant' : plant})

def post_plant(request):
    form = PlantForm(request.POST)
    if form.is_valid():
        form.save(commit = True)    
    return HttpResponseRedirect('/')