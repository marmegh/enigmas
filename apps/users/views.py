# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User
from ..thing.models import Trip, Join
import bcrypt

# Create your views here.
def index(request):
    #start the journey
    login = LoginForm()
    register = RegistrationForm()
    return render(request, 'users/index.html', {'login':login, 'register': register})
def create(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
    #process registration form to add an account
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpw = request.POST['cpw']
        hash1 = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        User.objects.create(name = name, username = username, email = email, password = hash1)
        temp = User.objects.get(email = email)
        request.session['id'] = temp.id
        return redirect('/dashboard')
def login(request):
    # process login form
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        username = request.POST['username']
        temp = User.objects.get(username = username)
        request.session['id'] = temp.id
        print request.session['id']
        return redirect('/dashboard')
def dashboard(request):
    id = request.session['id']
    user = User.objects.get(id = id)
    alltrips = Trip.objects.all()
    othertrips = alltrips.exclude(planner=user)
    joins = Join.objects.filter(joiner = user)
    otherjoins = Join.objects.exclude(joiner = user)
    myjoins = Trip.objects.filter(joins = joins)
    prospective = othertrips.exclude(joins = joins)
    mytrips = Trip.objects.filter(planner = user)
    context = {
        'id':id,
        'name': user.name,
        'mytrips': mytrips,
        'myjoins': joins,
        'alltrips': prospective,
    }
    return render(request, 'users/dashboard.html', context)
def logout(request):
    del request.session['id']
    return redirect('/')
