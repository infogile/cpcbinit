from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.
class InlineInstitue(admin.TabularInline):
    model = Institute
    max_num = 1

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('lat','long','inspection','createdon','updatedon')

admin.site.site_header = "CPCB Administration"
admin.site.site_title = "CPCB Admin"
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'token')
    inlines = [InlineInstitue]

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('assigned_to','factory')

admin.site.register(User, UserAdmin)


admin.site.register(Basin)
admin.site.register(State)
admin.site.register(Institute)
admin.site.register(SPCB)
admin.site.register(Headoffice)
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(Factories)
admin.site.register(Inspection,InspectionAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Field_report)
admin.site.register(Field_report_images)
admin.site.register(Field_report_poc)
admin.site.register(Inspection_report)
admin.site.register(Action)
admin.site.register(Action_report)
admin.site.register(Action_report_files)
admin.site.register(Inspection_report_data)
admin.site.register(my_status)
