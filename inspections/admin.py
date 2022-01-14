from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.
class InlineInstitue(admin.TabularInline):
    model = Institute
    max_num = 1

class Inspection_report_tabular(admin.TabularInline):
    model = Inspection_report
    can_delete = False
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        return Inspection_report.objects.filter(inspection=obj).count()

class Inspection_report_dataTabular(admin.TabularInline):
    model = Inspection_report_data
    can_delete = False
    extra = 0
    fields = [('ZLDnorms','bod','bodLoad'),('cod','codLoad'),'complianceStatus',
    ('defunctETP','dilutionInETP'),('dissentBypassArrangement','dissentWaterDischarge'),
    'effluent','finalRecommendation']

    def get_max_num(self, request, obj=None, **kwargs):
        return Inspection_report_data.objects.filter(inspection=obj).count()
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
    list_display = ('assigned_to',Inspection.code,'factory')
    list_filter = ('assigned_to','status','factory__status',)
    inlines = [Inspection_report_tabular,Inspection_report_dataTabular]
    search_fields = ('factory__name','factory__unitcode',)

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('unitcode','name','state','district','status')
    list_filter = ('state','status','sector',)
    search_fields = ('name','unitcode')

class FieldReportImage(admin.ModelAdmin):
    list_display = ('field_report','image')
    list_filter = ('field_report__inspection__assigned_to',)
    search_fields = ('field_report__inspection__factory__name','field_report__inspection__factory__unitcode')

class FieldImage(admin.TabularInline):
    model = Field_report_images
    can_delete = False
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        return Field_report_images.objects.filter(field_report=obj).count()


class FieldReportAdmin(admin.ModelAdmin):
    list_display = ('id',Field_report.unitcode,'inspection',Field_report.assigned,)
    list_filter = ('inspection__assigned_to','inspection__factory__status')
    inlines = [FieldImage]
    search_fields = ('inspection__factory__name','inspection__factory__unitcode')

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

class Inspection_reportAdmin(admin.ModelAdmin):
    list_display = ('id','inspection')
    list_filter = ('inspection__assigned_to__institute',)
    search_fields = ('inspection__factory__name','inspection__factory__unitcode')


class Inspection_report_dataAdmin(admin.ModelAdmin):
    list_display = ('id',Inspection_report_data.code,'inspection',)
    list_filter = ('inspection__assigned_to__institute',)
    search_fields = ('inspection__factory__name','inspection__factory__unitcode',)

class allinspectionResponse(admin.ModelAdmin):
    list_display = ('id','inspections','action_report',)
    list_filter = ('inspections__assigned_to__institute',)
    search_fields = ('inspections__factory__name',)

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
admin.site.register(Inspection_report,Inspection_reportAdmin)
# admin.site.register(Action)
admin.site.register(Action_report)
admin.site.register(Action_report_files)
admin.site.register(Inspection_report_data,Inspection_report_dataAdmin)
admin.site.register(my_status)
admin.site.register(allinspection_response,allinspectionResponse)
