from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.context_processors import csrf

def index(request):
    return render(request, 'virt_tours/index.html')

def register(request):
    return render(request, 'virt_tours/register.html')

def login_page(request):
    return render(request, 'virt_tours/login.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'virt_tours/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('virt_tours/loggedin.html',
                             {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('virt_tours/invalid_login.html')

def logout(request):
    logout(request)
    return render_to_response('virt_tours/logout.html')
