import datetime

from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def index(request):
    # sleepy.delay(5)
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
        form = trucksForms(request.POST, request.FILES)
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
                title=request.FILES['title'],
                insurance_card=request.FILES['insurance_card'],
            )
            truck_info.save()
            return redirect('index')
    else:
        form = trucksForms()
        return render(request, 'Inventory/add_new.html', {'form': form})


def addSmallVehicles(request):
    data = request.POST
    if request.method == "POST":
        form = smallVehiclesForm(request.POST, request.FILES)
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
                status=data['status'], title=request.FILES['title'],
                insurance_card=request.FILES['insurance_card'],
            )
            smallVehicles_info.save()
            return redirect('index')
    else:
        form = smallVehiclesForm()
        return render(request, 'Inventory/add_new.html', {'form': form})


def editTrucks(request, pk):
    item = get_object_or_404(trucks, pk=pk)

    if request.method == "POST":
        form = trucksForms(request.POST or None, request.FILES or None, instance=item)
        data = request.POST
        if form.is_valid():
            try:
                truck = trucks.objects.get(vin=data['vin'])
                truck.nickname = data['nickname']
                truck.make = data['make']
                truck.model = data['model']
                truck.type = data['type']
                truck.plate = data['plate']
                truck.ezPass = data['ezPass']
                truck.mileage = data['mileage']
                truck.reportedProblem = data['reportedProblem']
                truck.inspection = convert_date(data['inspection'])
                truck.registration = convert_date(data['registration'])
                truck.oilChange = data['oilChange']
                truck.isMonitored = data['isMonitored']
                truck.status = data['status']
                truck.title = request.FILES['title']
                truck.insurance_card = request.FILES['insurance_card']
                truck.save()

            except FileNotFoundError:
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
                    title=request.FILES['title'],
                    insurance_card=request.FILES['insurance_card']
                )
                truck_info.save()
            return redirect('index')
    else:
        form = trucksForms(instance=item)
        return render(request, 'Inventory/edit_items.html', {'form': form})


def editSmallVehicles(request, pk):
    item = get_object_or_404(smallVehicles, pk=pk)

    if request.method == "POST":
        print(request.FILES)
        form = smallVehiclesForm(request.POST, instance=item)
        data = request.POST
        if form.is_valid():
            try:
                car = smallVehicles.objects.get(vin=data['vin'])
                car.nickname = data['nickname']
                car.make = data['make']
                car.model = data['model']
                car.type = data['type']
                car.plate = data['plate']
                car.ezPass = data['ezPass']
                car.mileage = data['mileage']
                car.reportedProblem = data['reportedProblem']
                car.inspection = convert_date(data['inspection'])
                car.registration = convert_date(data['registration'])
                car.oilChange = data['oilChange']
                car.isMonitored = data['isMonitored']
                car.status = data['status']
                car.title.get = request.FILES['title']
                car.insurance_card.get = request.FILES['insurance_card']
                car.save()

            except FileNotFoundError:
                car_info = smallVehicles(
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
                    title=request.FILES['title'],
                    insurance_card=request.FILES['insurance_card']
                )
                car_info.save()
            # except Exception as e:
            #     print(e)
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


def TruckDetailView(request, pk):
    items = trucks.objects.filter(pk=pk)
    context = {'items': items}

    return render(request, 'Inventory/truck_details.html', context)


def VehicleDetailView(request, pk):
    items = smallVehicles.objects.filter(pk=pk)
    context = {'items': items}

    return render(request, 'Inventory/vehicle_details.html', context)
