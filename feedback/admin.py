from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedbackText', 'postTime', 'updateTime', 'sentByParent')
    
    
admin.site.register(Feedback, FeedbackAdmin)