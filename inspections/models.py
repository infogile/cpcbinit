from typing import Match
from django.contrib.admin.decorators import action
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.lookups import In
from django.contrib.auth.hashers import make_password, check_password
import uuid
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255,unique=True,default="None")

    def __str__(self):
        return self.username    

    def save(self,*args, **kwargs):    #password hashed everytime save is called
        if not User.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = User.objects.last().id +1 
        self.password = make_password(self.password)
        self.token = uuid.uuid4()
        super().save(*args, **kwargs)



class Basin(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not Basin.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Basin.objects.last().id +1 
        super().save(*args, **kwargs)

class State(models.Model):
    short_name = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not State.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = State.objects.last().id +1 
        super().save(*args, **kwargs)

class Institute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=100)
    poc = models.CharField(max_length=40)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return(self.institute)
    def save(self,*args, **kwargs):
        if not Institute.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Institute.objects.last().id +1 
        super().save(*args, **kwargs)

class SPCB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return(self.state)
    def save(self,*args, **kwargs):
        if not SPCB.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = SPCB.objects.last().id +1 
        super().save(*args, **kwargs)

class Headoffice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not Headoffice.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Headoffice.objects.last().id +1 
        super().save(*args, **kwargs)


class District(models.Model):
    short_code = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not District.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = District.objects.last().id +1 
        super().save(*args, **kwargs)

class Sector(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not Sector.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Sector.objects.last().id +1 
        super().save(*args, **kwargs)


class Factories(models.Model):
    name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    unitcode = models.CharField(max_length=10,unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    region = models.CharField(max_length=30)
    basin = models.ForeignKey(Basin, on_delete=models.CASCADE)
    status = models.IntegerField(default = 0, choices=[(0,"inspection yet to be taken"),(1,"inspection taken from app"),(2,"inspection report uploaded on web"),(3,"action taken by state authorties"),(4,"factory closed")])
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not Factories.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Factories.objects.last().id +1 
        super().save(*args, **kwargs)

class my_status(models.Model):
    total_assigned = models.IntegerField(default=0)
    total_inspected = models.IntegerField(default=0)
    total_factory_closed = models.IntegerField(default=0)
    bypass = models.IntegerField(default=0)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.institute.institute
    def save(self,*args, **kwargs):
        if not my_status.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = my_status.objects.last().id +1 
        super().save(*args, **kwargs)
class Inspection(models.Model):
    status = models.IntegerField()
    factory = models.ForeignKey(Factories, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Institute, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    def __str__(self):
        return(self.factory.name)
    
    def save(self, *args, **kwargs):
        if not Inspection.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Inspection.objects.last().id +1 

        if not self.pk:
            status = my_status.objects.filter(institute = self.assigned_to).first()
            if(status == None):
                status = my_status.objects.create(institute = self.assigned_to)
                status.total_assigned +=1
                status.save()
                super(Inspection,self).save(*args, **kwargs)
            
            status.total_assigned +=1
            status.save()
        super(Inspection,self).save(*args, **kwargs)


class Attendance(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now=True)
    updatedon = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.inspection))
    def save(self,*args, **kwargs):
        if not Attendance.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Attendance.objects.last().id +1 
        super().save(*args, **kwargs)


class Field_report(models.Model):
    uos = models.CharField(max_length=255)
    uosdetail = models.CharField(max_length=255)
    etpos = models.CharField(max_length=255)
    etposdetail = models.CharField(max_length=255)
    cpc = models.CharField(max_length=255)
    ipc = models.CharField(max_length=255)
    ppopd = models.CharField(max_length=255)
    fwwpdbofm = models.CharField(max_length=255)
    ocs = models.CharField(max_length=255)
    sonfc = models.CharField(max_length=255)
    mrr = models.CharField(max_length=255)
    mrrname = models.CharField(max_length=40)
    csac = models.CharField(max_length=255)
    wc = models.CharField(max_length=255)
    hc = models.CharField(max_length=255)
    cc = models.CharField(max_length=255)
    sfwc = models.CharField(max_length=255)
    sfwcdetail = models.CharField(max_length=255)
    fib = models.CharField(max_length=255)
    fibdetail = models.CharField(max_length=255)
    fietpinlet = models.CharField(max_length=255)
    fietpinletdetail = models.CharField(max_length=255)
    fietpoutlent = models.CharField(max_length=255)
    fietpoutlentdetail = models.CharField(max_length=255)
    fmetpoutletcdf = models.CharField(max_length=255)
    fmetpoutletpdf = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    osdetail = models.CharField(max_length=255)
    semfetp = models.CharField(max_length=255)
    semfer = models.CharField(max_length=255)
    specificobservations = models.TextField()
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now=True)
    updatedon = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return(str(self.inspection))
    def assigned(self):
        return(str(self.inspection.assigned_to))
    def save(self,*args, **kwargs):
        if not Field_report.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Field_report.objects.last().id +1 
        super().save(*args, **kwargs)

def upload_to(instance,filename):
    id = uuid.uuid4()
    user = instance.field_report.inspection
    return 'posts/inspection_{user}/{id}.jpeg'.format(id=id,user=user)
class Field_report_images(models.Model):
    image = models.ImageField(_("Image"),upload_to=upload_to,default = 'posts/default.jpg',blank = True)
    field_report = models.ForeignKey(Field_report, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.field_report))
    def save(self,*args, **kwargs):
        if not Field_report_images.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Field_report_images.objects.last().id +1 
        super().save(*args, **kwargs)


class Field_report_poc(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    number = models.IntegerField()
    field_report = models.ForeignKey(Field_report, on_delete=models.CASCADE)
    def __str__(self):
        return(self.name)
    def save(self,*args, **kwargs):
        if not Field_report_poc.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Field_report_poc.objects.last().id +1 
        super().save(*args, **kwargs)

class Inspection_report(models.Model):
    file = models.FileField()
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.inspection))
    def save(self,*args, **kwargs):
        if not Inspection_report.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Inspection_report.objects.last().id +1 
        super().save(*args, **kwargs)

class Action(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    def __str__(self):
        return(str(self.inspection))
    def save(self,*args, **kwargs):
        if not Action.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Action.objects.last().id +1 
        super().save(*args, **kwargs)

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
    def save(self,*args, **kwargs):
        if not Action_report.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Action_report.objects.last().id +1 
        super().save(*args, **kwargs)

class Action_report_files(models.Model):
    file = models.FileField()
    action_report = models.ForeignKey(Action_report, on_delete=models.CASCADE)
    def __str__(self):
        return(str(self.action_report))
    def save(self,*args, **kwargs):
        if not Action_report_files.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Action_report_files.objects.last().id +1 
        super().save(*args, **kwargs)

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
    def save(self,*args, **kwargs):
        if not Inspection_report_data.objects.count():
            self.id = 1
        else:
            if not self.pk:
                self.id = Inspection_report_data.objects.last().id +1 
        super().save(*args, **kwargs)
    





