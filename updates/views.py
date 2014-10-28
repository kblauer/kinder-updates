from django.shortcuts import render_to_response, get_object_or_404
from updates.models import Update
from forms import UpdateForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.core import serializers
# Create your views here.


def all_updates(request):
    username = None
    group = 'parent'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('updates.add_update'):
            group = 'teacher'
            
    return render_to_response('all_updates.html',
                              {'updates' : Update.objects.all(),
                               'username' : username, 'group' : group})
    
def update(request, update_id):
    username = None
    group = 'parent'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('updates.add_update'):
            group = 'teacher'
            
    update = get_object_or_404(Update, pk=update_id)
    
    return render_to_response('update.html',
                              {'update' : update,
                               'username' : username, 'group' : group})
    
def create(request):
    username = None
    group = 'parent'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('updates.add_update'):
            group = 'teacher'
            
    if request.POST:
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/updates/all')
        
    else:
        form = UpdateForm()
        
        args = {}
        args.update(csrf(request))
        
        args['form'] = form
        args['username'] = username
        args['group'] = group
        
        return render_to_response('create_update.html', args)
    
    
def json_all(request):
    updates = Update.objects.all()
    data = serializers.serialize("json", updates)
    return HttpResponse(data, content_type='application/json')


