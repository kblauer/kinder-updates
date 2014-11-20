from django.contrib import admin
from kids.models import Kid


class KidAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',)
    
    
admin.site.register(Kid, KidAdmin)