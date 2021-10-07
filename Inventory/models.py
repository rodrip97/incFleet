from django.db import models


# All Trucks (Flatbeds, booms whatever, not pick ups)
class trucks(models.Model):
    nickname = models.CharField(blank=False, null=True, default=None, max_length=80)
    make = models.CharField(blank=False, null=True, default=None, max_length=80)
    model = models.CharField(blank=False, null=True, default=None, max_length=80)
    type = models.CharField(blank=False, null=True, default=None, max_length=80)
    plate = models.CharField(blank=False, null=True, default=None, max_length=80)
    vin = models.CharField(blank=False, null=True, default=None, max_length=80)
    ezPass = models.CharField(blank=False, null=True, default=None, max_length=80)
    mileage = models.CharField(blank=False, null=True, default=None, max_length=80)
    reportedProblem = models.CharField(blank=False, null=True, default=None, max_length=80)
    inspection = models.DateField(blank=False, null=True, default=None)
    registration = models.DateField(blank=False, null=True, default=None)
    oilChange = models.CharField(blank=False, null=True, default=None, max_length=80)
    isMonitored = models.CharField(blank=False, null=True, default=None, max_length=80)
    status = models.CharField(blank=False, null=True, default=None, max_length=80)

    def __str__(self):
        return 'Nickname: {0}'.format(self.nickname)


# for vans and personal cars EG: Omesh Kia or Mohammed Pick up truck
class smallVehicles(models.Model):
    nickname = models.CharField(blank=False, null=True, default=None, max_length=80)
    make = models.CharField(blank=False, null=True, default=None, max_length=80)
    model = models.CharField(blank=False, null=True, default=None, max_length=80)
    type = models.CharField(blank=False, null=True, default=None, max_length=80)
    plate = models.CharField(blank=False, null=True, default=None, max_length=80)
    vin = models.CharField(blank=False, null=True, default=None, max_length=80)
    ezPass = models.CharField(blank=False, null=True, default=None, max_length=80)
    mileage = models.CharField(blank=False, null=True, default=None, max_length=80)
    reportedProblem = models.CharField(blank=False, null=True, default=None, max_length=80)
    inspection = models.DateField(blank=False, null=True, default=None, max_length=80)
    registration = models.DateField(blank=False, null=True, default=None, max_length=80)
    oilChange = models.CharField(blank=False, null=True, default=None, max_length=80)
    isMonitored = models.CharField(blank=False, null=True, default=None, max_length=80)
    status = models.CharField(blank=False, null=True, default=None, max_length=80)

    def __str__(self):
        return 'Nickname: {0}'.format(self.nickname)
