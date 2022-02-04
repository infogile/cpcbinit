from django.contrib.admin import SimpleListFilter
from .models import *
from django.utils.translation import gettext_lazy as _

class SPCB_user_filter(SimpleListFilter):
    title = _('created_by')
    parameter_name = 'created_by'

    def lookups(self,request,model_admin):
        users = User.objects.filter(role='spcb_user')
        return [(user.id,_(user.username)) for user in users]

    def queryset(self,request,queryset):
            if self.value():
                return queryset.filter(created_by=self.value())
            else:
                return queryset
