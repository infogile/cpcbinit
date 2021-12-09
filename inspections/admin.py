from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.
class InlineInstitue(admin.TabularInline):
    model = Institute
    max_num = 1

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('lat','long','inspection','createdon','updatedon')
    list_filter = ('inspection',)

admin.site.site_header = "CPCB Administration"
admin.site.site_title = "CPCB Admin"
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'token')
    inlines = [InlineInstitue]

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('assigned_to','factory')
    list_filter = ('assigned_to',)

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name','state','district','status')
    list_filter = ('state','district','status',)

class FieldReportImage(admin.ModelAdmin):
    list_display = ('field_report','image')
    list_filter = ('field_report',)

class FieldImage(admin.TabularInline):
    model = Field_report_images
    can_delete = False
class FieldReportAdmin(admin.ModelAdmin):
    list_display = ('id','inspection',Field_report.assigned,)
    list_filter = ('inspection',)
    inlines = [FieldImage]

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('short_code','name','state')
    list_filter = ('state',)

class InlineMystatus(admin.TabularInline):
    model = my_status
    max_num = 1

# class InlineInspection(admin.TabularInline):
#     model = Inspection
#     can_delete = True
#     list_per_page = 5
class IntituteView(admin.ModelAdmin):
    list_display = ('institute','user','poc','state')
    list_filter = ('state',)
    inlines = [InlineMystatus]

admin.site.register(User, UserAdmin)


admin.site.register(Basin)
admin.site.register(State)
admin.site.register(Institute,IntituteView)
admin.site.register(SPCB)
admin.site.register(Headoffice)
admin.site.register(District,DistrictAdmin)
admin.site.register(Sector)
admin.site.register(Factories,FactoryAdmin)
admin.site.register(Inspection,InspectionAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Field_report,FieldReportAdmin)
admin.site.register(Field_report_images,FieldReportImage)
admin.site.register(Field_report_poc)
admin.site.register(Inspection_report)
admin.site.register(Action)
admin.site.register(Action_report)
admin.site.register(Action_report_files)
admin.site.register(Inspection_report_data)
admin.site.register(my_status)
