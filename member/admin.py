from django.contrib import admin



from .models import  Tblmain,Class1, Registration

class Class1Admin(admin.ModelAdmin):
    list_display = ('classnumber','name','department')
    search_fields = ['name']
    #readonly_fields = ('department','name')
    list_per_page = 30
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('registrationnumber', 'classnumber', 'mem_id')
    #readonly_fields = ('registrationnumber',)
    search_fields = ['registrationnumber']
    list_per_page = 20
class TblMainAdmin(admin.ModelAdmin):
    list_display = ('mem_id','firstname','lastname')
    search_fields = ['mem_id','firstname','lastname']
    list_per_page = 10
    #readonly_fields = ('mem_id','firstname','lastname',)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Tblmain,TblMainAdmin)
admin.site.register(Class1,Class1Admin)