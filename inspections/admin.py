from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'token')

admin.site.register(User, UserAdmin)

admin.site.register(Basin)
admin.site.register(State)
admin.site.register(Institute)
admin.site.register(SPCB)
admin.site.register(Headoffice)
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(Factories)
admin.site.register(Inspection)
admin.site.register(Attendance)
admin.site.register(Field_report)
admin.site.register(Field_report_images)
admin.site.register(Field_report_poc)
admin.site.register(Inspection_report)
admin.site.register(Action)
admin.site.register(Action_report)
admin.site.register(Action_report_files)
admin.site.register(Inspection_report_data)
