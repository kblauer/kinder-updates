from django.shortcuts import render_to_response, get_object_or_404
from feedback.models import Feedback
from forms import FeedbackForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.core import serializers
# Create your views here.


def all_feedback(request):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
            
    return render_to_response('all_feedback.html',
                              {'feedback' : Feedback.objects.all(),
                               'username' : username, 'group' : group})
    
def feedback(request, fb_id):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
            
    feedback = get_object_or_404(Feedback, pk=fb_id)
    
    return render_to_response('feedback.html',
                              {'feedback' : feedback,
                               'username' : username, 'group' : group})
    
def create(request):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
            
    if request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # this saves the form submission data, but doesn't submit it to the server yet
            # It is needed so that we can set the parent ID on the model data before final submission
            fb = form.save(commit=False)
            fb.sentByParent = request.user
            fb.save()
            
            return HttpResponseRedirect('/feedback/parent_view/')
        
    else:
        form = FeedbackForm()
        
        args = {}
        args.update(csrf(request))
        
        args['form'] = form
        args['username'] = username
        args['group'] = group
        
        return render_to_response('create_feedback.html', args)
    
    
def parent_view(request):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
            
    parentFeedback = Feedback.objects.filter(sentByParent=request.user)
    
    if not parentFeedback:
        return HttpResponseRedirect('/feedback/parent_view_error/')
    
    return render_to_response('all_feedback.html', 
                              {'feedback' : parentFeedback,
                               'username' : username, 'group' : group})
    
def parent_view_error(request):
    username = None
    group = 'teacher'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('feedback.add_feedback'):
            group = 'parent'
            
    return render_to_response('parent_error.html', 
                              {'username' : username, 'group' : group})
    
def json_all(request):
    feedback = Feedback.objects.all()
    data = serializers.serialize("json", feedback)
    return HttpResponse(data, content_type='application/json')


