from django.contrib import admin
from attendance.models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('attDate', 'didAtt', 'updateTime')
    
    
admin.site.register(Attendance, AttendanceAdmin)