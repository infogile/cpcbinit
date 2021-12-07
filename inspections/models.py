from typing import Match
from django.contrib.admin.decorators import action
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
from django.db.models.lookups import In

# Create your models here.
    

class Basin(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return(self.name)

class State(models.Model):
    short_name = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    def __str__(self):
        return(self.name)

class Institute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=100)
    poc = models.CharField(max_length=40)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return(self.institute)

class SPCB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return(self.state)

class Headoffice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return(self.name)


class District(models.Model):
    short_code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return(self.District)

class Sector(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return(self.name)


class Factories(models.Model):
    name = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    unitcode = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    region = models.CharField(max_length=30)
    basin = models.ForeignKey(Basin, on_delete=models.CASCADE)
    def __str__(self):
        return(self.name)


class Inspection(models.Model):
    status = models.IntegerField()
    factory = models.ForeignKey(Factories, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Institute, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    def __str__(self):
        return(self.factory)



class Attendance(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.inspection))


class Field_report(models.Model):
    uos = models.CharField(max_length=20)
    uosdetail = models.CharField(max_length=20)
    etpos = models.CharField(max_length=20)
    etposdetail = models.CharField(max_length=20)
    cpc = models.CharField(max_length=20)
    ipc = models.CharField(max_length=20)
    ppopd = models.CharField(max_length=20)
    fwwpdbofm = models.CharField(max_length=20)
    ocs = models.CharField(max_length=20)
    sonfc = models.CharField(max_length=20)
    mrr = models.CharField(max_length=20)
    mrrname = models.CharField(max_length=40)
    csac = models.CharField(max_length=20)
    wc = models.CharField(max_length=20)
    hc = models.CharField(max_length=20)
    cc = models.CharField(max_length=20)
    sfwc = models.CharField(max_length=20)
    sfwcdetail = models.CharField(max_length=40)
    fib = models.CharField(max_length=20)
    fibdetail = models.CharField(max_length=20)
    fietpinlet = models.CharField(max_length=20)
    fietpinletdetail = models.CharField(max_length=20)
    fietpoutlent = models.CharField(max_length=20)
    fietpoutlentdetail = models.CharField(max_length=20)
    fmetpoutletcdf = models.CharField(max_length=20)
    fmetpoutletpdf = models.CharField(max_length=20)
    os = models.CharField(max_length=20)
    osdetail = models.CharField(max_length=20)
    semfetp = models.CharField(max_length=20)
    semfer = models.CharField(max_length=20)
    specificobservations = models.CharField(max_length=40)
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.inspection))


class Field_report_images(models.Model):
    image = models.ImageField()
    field_report = models.ForeignKey(Field_report, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.field_report))

class Field_report_poc(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    number = models.IntegerField()
    field_report = models.ForeignKey(Field_report, on_delete=models.CASCADE)
    def __str__(self):
        return(self.name)

class Inspection_report(models.Model):
    file = models.FileField()
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.inspection))

class Action(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    def __str__(self):
        return(str(self.inspection))

class Action_report(models.Model):
    compliance_status = models.IntegerField()
    showcausenoticestatus = models.BooleanField()
    date = models.DateField()
    finalrecommendation = models.CharField(max_length=200)
    created_by = models.ForeignKey(SPCB, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.action))

class Action_report_files(models.Model):
    file = models.FileField()
    action_report = models.ForeignKey(Action_report, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.action_report))

class Inspection_report_data(models.Model):
    ZLDnorms = models.CharField(max_length=20)
    bod = models.CharField(max_length=20)
    bodLoad = models.CharField(max_length=20)
    cod = models.CharField(max_length=20)
    codLoad = models.CharField(max_length=20)
    complianceStatus = models.IntegerField()
    defunctETP = models.BooleanField()
    dilutionInETP = models.BooleanField()
    dissentBypassArrangement = models.BooleanField()
    dissentWaterDischarge = models.BooleanField()
    effluent = models.BooleanField()
    finalRecommendation = models.CharField(max_length=20)
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.inspection))





