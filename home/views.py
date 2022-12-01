from django.shortcuts import render
from pathlib import Path
import pickle

# Create your views here.

def home_view(request):
    return render(request,'index.html')

def result(request):
    BASE_DIR = str(Path(__file__).resolve().parent.parent)
    with open(BASE_DIR+'/home/model_pkl', 'rb') as f:
        lr = pickle.load(f)
    room_type = float(request.POST.get('room_type'))
    hotel_type = float(request.POST.get('hotel_type'))
    z = [room_type, hotel_type]
    out = lr.predict([z]).astype(int)
    price = 'The predicted price is '+ str(out[0])
    return render(request, "index.html", {'prediction_result':price})

def home_about(request):
    return render(request, 'about.html')


def home_services(request):
    return render(request, 'services.html')

def home_contact(request):
    return render(request, 'contact.html')


