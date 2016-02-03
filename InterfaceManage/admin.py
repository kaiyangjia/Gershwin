from django.contrib import admin

# Register your models here.
from InterfaceManage.models import ItInterface, ItInterfaceField, ItModule, ItProject, ItRecord

admin.site.register(ItInterface)
admin.site.register(ItInterfaceField)
admin.site.register(ItModule)
admin.site.register(ItProject)
admin.site.register(ItRecord)