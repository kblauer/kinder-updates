from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext

def home(request):
    username = None
    group = 'parent'
    
    if request.user.is_authenticated():
        username = request.user.username
        if request.user.has_perm('updates.add_update'):
            group = 'teacher'
        
    
    #cs = {}
    #cs.update(csrf(request))
    return render_to_response('home.html',
                              {'username' : username, 'group' : group}, 
                              context_instance=RequestContext(request))

def auth_view(request):
    # retrieve the username and password from the POST request
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    # get the user object, or None if the user does not exist
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/user/invalid')
    
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')