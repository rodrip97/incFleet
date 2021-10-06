import datetime

from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def index(request):
    return render(request, 'Inventory/index.html')


def displayTrucks(request):
    items = trucks.objects.all()
    context = {'items': items, 'header': 'trucks'}
    return render(request, 'Inventory/index.html', context)


def displaySmallVehicles(request):
    items = smallVehicles.objects.all()
    context = {'items': items, 'header': 'cars'}
    return render(request, 'Inventory/index.html', context)


def convert_date(date_input):
    pre_date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
    return pre_date.strftime("%Y-%m-%d")


def addTrucks(request):
    data = request.POST
    if request.method == "POST":
        form = trucksForms(request.POST)
        if form.is_valid():
            truck_info = trucks(
                nickname=data['inspection'],
                make=data['inspection'],
                model=data['inspection'],
                type=data['inspection'],
                plate=data['inspection'],
                vin=data['inspection'],
                ezPass=data['inspection'],
                mileage=data['inspection'],
                reportedProblem=data['inspection'],
                inspection=convert_date(data['inspection']),
                registration=convert_date(data['registration']),
                oilChange=data['inspection'],
                isMonitored=data['inspection'],
                status=data['inspection'],
            )
            truck_info.save()
            return redirect('index')
    else:
        form = trucksForms()
        return render(request, 'Inventory/add_new.html', {'form': form})


def addSmallVehicles(request):
    if request.method == "POST":
        form = smallVehiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = smallVehiclesForm()
        return render(request, 'Inventory/add_new', {'form': form})


def editItem(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)
        return render(request, 'Inventory/edit_items.html', {'form': form})


def editTrucks(request, pk):
    return editItem(request, pk, trucks, trucksForms)


def editSmallVehicles(request, pk):
    return editItem(request, pk, smallVehicles, smallVehiclesForm)
