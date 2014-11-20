import datetime

from django.core import serializers
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone

from attendance.models import Attendance
from forms import AttendanceForm


# Create your views here.
def attendance_today(request):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
    
    endDate = timezone.now()
    startDate = endDate - datetime.timedelta(days=1) 
    
    todayAtt = Attendance.objects.filter(attDate__range=(startDate, endDate))
            
    return render_to_response('att_today.html',
                              {'att' : todayAtt,
                               'username' : username, 'group' : group})
    
    
def attendance_single(request, att_id):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
            
    att = get_object_or_404(Attendance, pk=att_id)
                
    return render_to_response('att_today.html',
                              {'att' : att,
                               'username' : username, 'group' : group})
    
    
def create(request):
    username = None
    group = 'parent'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('updates.add_update'):
            group = 'teacher'
            
    if request.POST:
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/att/today/')
        
    else:
        form = AttendanceForm()
        
        args = {}
        args.update(csrf(request))
        
        args['form'] = form
        args['username'] = username
        args['group'] = group
        
        return render_to_response('create_attendance.html', args)
    
    

    
    
    
def json_all(request):
    attendance = Attendance.objects.all()
    data = serializers.serialize("json", attendance)
    return HttpResponse(data, content_type='application/json')
