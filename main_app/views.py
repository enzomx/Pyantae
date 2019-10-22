from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Plant
from .models import Dataplant
from .forms import PlantForm

import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    plants = Plant.objects.all()
 #   dataplantrt = Dataplant.objects.all()
    
#    dataplantrts = Dataplant.objects.latest('dataplant_date')
    dataplantrt = []

    for plant in plants:
        dataplantrt.append(Dataplant.objects.all().filter(plant_id=plant.id).order_by('-dataplant_date')[0])
            
    zipped = zip(plants, dataplantrt)
 
    return render(request, 'index.html', {'plants' : plants, 'all' : zipped})

def show(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    
    dataplantrt = Dataplant.objects.all().filter(plant_id=plant.id).order_by('-dataplant_date')[0]
    
    return render(request, 'show.html', {'plant' : plant, 'plant_last' : dataplantrt})

def post_plant(request):
    form = PlantForm(request.POST)
    if form.is_valid():
        form.save(commit = True)    
    return HttpResponseRedirect('/')

def generargrafico(request, plant_id):
    
    datosgrafico = Dataplant.objects.all().filter(plant_id=plant_id)

    #records = Dataplant.objects.get(id=plant_id)
    dat = []
    fecha = []
    hum = []
    tem = []
    hi = []
    lum = []
    
    for data in datosgrafico:
        fecha.append(datetime(data.dataplant_date.year, data.dataplant_date.month, data.dataplant_date.day, data.dataplant_date.hour, data.dataplant_date.minute))
        hum.append(data.plant_hum)
        tem.append(data.plant_temp)
        hi.append(data.plant_hi)
        lum.append(data.plant_light)
        
    
    dat.append([fecha, hum])
    dat.append([fecha, tem])
    dat.append([fecha, lum])
        
    #el tercer parametro es el tamaño de la imagen en pixeles/1000
    graficos = ['Humedad', 'Temperatura', 'Luminosidad']
    
    colores = ["y", "g","r"]

    figsize = (9, 7)
    cols = 2
    rows = len(graficos) // cols + 1

    fig, axs = plt.subplots(rows, cols, figsize=figsize, constrained_layout=True)

    axsTemp = axs.flat
    for ax in axsTemp[len(graficos):]:
        ax.remove()
    axs = axsTemp[:len(graficos)]
    
    for ax, grafico, color, d in zip(axs, graficos, colores, dat):
        ax.set_title(grafico)
        ax.plot(d[0], d[1], color=color, dashes=[2, 2, 10, 2], )

    buf = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)

    response = HttpResponse(buf.getvalue(), content_type='image/png')

    fig.clear()

    response['Content-Length'] = str(len(response.content))

    return response
