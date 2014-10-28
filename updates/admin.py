from django.contrib import admin
from updates.models import Update


class UpdateAdmin(admin.ModelAdmin):
    list_display = ('updateText', 'postTime', 'updateTime')
    
    
admin.site.register(Update, UpdateAdmin)