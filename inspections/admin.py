from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.
class InlineInstitue(admin.TabularInline):
    model = Institute
    max_num = 1

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('lat','long','inspection','createdon','updatedon',)
    readonly_fields = ('createdon','updatedon',)
    list_filter = ('inspection__assigned_to',)
    search_fields = ('inspection__factory__name',)

admin.site.site_header = "CPCB Administration"
admin.site.site_title = "CPCB Admin"
admin.site.index_title = "Welcome to CPCB Admin powered by CloverBuddies"
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'token')
    inlines = [InlineInstitue]

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('assigned_to','factory')
    list_filter = ('assigned_to','status')
    search_fields = ('factory__name',)

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name','state','district','status')
    list_filter = ('state','status','sector',)
    search_fields = ('name',)

class FieldReportImage(admin.ModelAdmin):
    list_display = ('field_report','image')
    list_filter = ('field_report__inspection__assigned_to',)
    search_fields = ('field_report__inspection__factory__name',)

class FieldImage(admin.TabularInline):
    model = Field_report_images
    can_delete = False
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        return Field_report_images.objects.filter(field_report=obj).count()


class FieldReportAdmin(admin.ModelAdmin):
    list_display = ('id','inspection',Field_report.assigned,)
    list_filter = ('inspection__assigned_to',)
    inlines = [FieldImage]
    search_fields = ('inspection__factory__name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('short_code','name','state')
    list_filter = ('state',)

class InlineMystatus(admin.TabularInline):
    model = my_status
    max_num = 1

class FieldReportPoc(admin.ModelAdmin):
    list_display = ('name','field_report')
    list_filter = ('field_report__inspection__assigned_to',)
    search_fields = ('field_report__inspection__factory__name',)

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
admin.site.register(Field_report_poc,FieldReportPoc)
admin.site.register(Inspection_report)
admin.site.register(Action)
admin.site.register(Action_report)
admin.site.register(Action_report_files)
admin.site.register(Inspection_report_data)
admin.site.register(my_status)
