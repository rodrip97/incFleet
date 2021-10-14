import datetime
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .tasks import sleepy


def index(request):
    #sleepy.delay(5)
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
    pre_date = datetime.strptime(date_input, '%Y-%m-%d')
    return pre_date.strftime("%Y-%m-%d")


def addTrucks(request):
    data = request.POST
    if request.method == "POST":
        form = trucksForms(request.POST)
        if form.is_valid():
            truck_info = trucks(
                nickname=data['nickname'],
                make=data['make'],
                model=data['model'],
                type=data['type'],
                plate=data['plate'],
                vin=data['vin'],
                ezPass=data['ezPass'],
                mileage=data['mileage'],
                reportedProblem=data['reportedProblem'],
                inspection=convert_date(data['inspection']),
                registration=convert_date(data['registration']),
                oilChange=data['oilChange'],
                isMonitored=data['isMonitored'],
                status=data['status'],
            )
            truck_info.save()
            return redirect('index')
    else:
        form = trucksForms()
        return render(request, 'Inventory/add_new.html', {'form': form})


def addSmallVehicles(request):
    data = request.POST
    if request.method == "POST":
        form = smallVehiclesForm(request.POST)
        if form.is_valid():
            smallVehicles_info = smallVehicles(
                nickname=data['nickname'],
                make=data['make'],
                model=data['model'],
                type=data['type'],
                plate=data['plate'],
                vin=data['vin'],
                ezPass=data['ezPass'],
                mileage=data['mileage'],
                reportedProblem=data['reportedProblem'],
                inspection=convert_date(data['inspection']),
                registration=convert_date(data['registration']),
                oilChange=data['oilChange'],
                isMonitored=data['isMonitored'],
                status=data['status'],
            )
            smallVehicles_info.save()
            return redirect('index')
    else:
        form = smallVehiclesForm()
        return render(request, 'Inventory/add_new.html', {'form': form})


def editTrucks(request, pk):
    item = get_object_or_404(trucks, pk=pk)

    if request.method == "POST":
        form = trucksForms(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = trucksForms(instance=item)
        return render(request, 'Inventory/edit_items.html', {'form': form})


def editSmallVehicles(request, pk):
    item = get_object_or_404(smallVehicles, pk=pk)

    if request.method == "POST":
        form = smallVehiclesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = smallVehiclesForm(instance=item)
        return render(request, 'Inventory/edit_items.html', {'form': form})


def deleteTrucks(request, pk):
    trucks.objects.filter(id=pk).delete()
    items = trucks.objects.all()
    context = {'items': items}

    return render(request, 'Inventory/index.html', context)


def deleteSmallVehicles(request, pk):
    smallVehicles.objects.filter(id=pk).delete()
    items = smallVehicles.objects.all()
    context = {'items': items}

    return render(request, 'Inventory/index.html', context)
