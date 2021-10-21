from datetime import datetime
from PIL import Image
from django.db import models


# All Trucks (Flatbeds, booms whatever, not pick ups)
class trucks(models.Model):
    TYPE_CHOICES = (('Sedan', 'Sedan'), ('Pickup', 'Pickup'), ('SUV', 'SUV'), ('Flatbed', 'Flatbed'))
    MON_CHOICES = (('Yes', 'Yes'), ('No', 'No'))

    nickname = models.CharField(blank=False, null=True, default=None, max_length=80)
    make = models.CharField(blank=False, null=True, default=None, max_length=80)
    model = models.CharField(blank=False, null=True, default=None, max_length=80)
    type = models.CharField(blank=False, null=True, choices=TYPE_CHOICES, default=None, max_length=80)
    plate = models.CharField(blank=False, null=True, default=None, max_length=80)
    vin = models.CharField(blank=False, null=True, default=None, max_length=80)
    ezPass = models.CharField(blank=False, null=True, default=None, max_length=80)
    mileage = models.CharField(blank=False, null=True, default=None, max_length=80)
    reportedProblem = models.CharField(blank=False, null=True, default=None, max_length=80)
    inspection = models.DateField(blank=False, null=True, default=None)
    registration = models.DateField(blank=False, null=True, default=None)
    oilChange = models.DateField(blank=False, null=True, default=None)
    isMonitored = models.CharField(blank=False, null=True, choices=MON_CHOICES, default=None, max_length=80)
    status = models.CharField(blank=False, null=True, default=None, max_length=80)
    title = models.ImageField(null=True, blank=True, upload_to='title_pics/')
    insurance_card = models.ImageField(null=True, blank=True, upload_to='insurance_cards/')

    def __str__(self):
        return format(self.nickname)


# def inspection_valid_check(self):
#    if self.inspection.strptime(self.inspection, "%d%m%y%H%M%S") > datetime.today().date():
#        self.inspection_active = True
#        self.save()
#        print('Inspection is valid!')
#    else:
#        self.inspection_active = False
#        print('Inspection is expired!')


# for vans and personal cars EG: Omesh Kia or Mohammed Pick up truck
class smallVehicles(models.Model):
    TYPE_CHOICES = (('Sedan', 'Sedan'), ('Pickup', 'Pickup'), ('SUV', 'SUV'))
    MON_CHOICES = (('Yes', 'Yes'), ('No', 'No'))

    nickname = models.CharField(blank=False, null=True, default=None, max_length=80)
    make = models.CharField(blank=False, null=True, default=None, max_length=80)
    model = models.CharField(blank=False, null=True, default=None, max_length=80)
    type = models.CharField(blank=False, null=True, choices=TYPE_CHOICES, default=None, max_length=80)
    plate = models.CharField(blank=False, null=True, default=None, max_length=80)
    vin = models.CharField(blank=False, null=True, default=None, max_length=80)
    ezPass = models.CharField(blank=False, null=True, default=None, max_length=80)
    mileage = models.CharField(blank=False, null=True, default=None, max_length=80)
    reportedProblem = models.CharField(blank=False, null=True, default=None, max_length=80)
    inspection = models.DateField(blank=False, null=True, default=None, max_length=80)
    registration = models.DateField(blank=False, null=True, default=None, max_length=80)
    oilChange = models.DateField(blank=False, null=True, default=None)
    isMonitored = models.CharField(blank=False, null=True, choices=MON_CHOICES, default=None, max_length=80)
    status = models.CharField(blank=False, null=True, default=None, max_length=80)
    title = models.ImageField(null=True, blank=True, upload_to='title_pics/')
    insurance_card = models.ImageField(null=True, blank=True, upload_to='insurance_cards/')

    # def inspection_valid_check(self):
    #    if self.inspection.strptime(self.inspection, "%d%m%y%H%M%S") > datetime.today().date():
    #        self.inspection_active = True
    #        self.save()
    #        print('Inspection is valid!')
    #    else:
    #        self.inspection_active = False
    #        print('Inspection is expired!')

    def __str__(self):
        return format(self.nickname)


class Permits(models.Model):
    permit_type_choices = (('Fire Hydrant', 'Fire Hydrant'), ('Parking', 'Parking'), ('Boom', 'Boom'))

    name = models.CharField(blank=False, null=False, default=None, max_length=80)
    type = models.CharField(blank=False, null=False, max_length=80, choices=permit_type_choices)
    address = models.CharField(blank=False, null=False, default=None, max_length=80)
    exp_date = models.DateField(blank=False, null=False, max_length=80)
