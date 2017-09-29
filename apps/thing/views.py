# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from ..users.models import User
from .models import Trip, Join
from django.shortcuts import render, HttpResponse, redirect
import datetime
from datetime import date

# Create your views here.
def add(request):
    return render(request, 'thing/thing.html')
def create(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/thing/add')
    else:
        destination = request.POST['destination']
        plan = request.POST['plan']
        start = request.POST['start']
        end = request.POST['end']
        user_id=request.session['id']
        user = User.objects.get(id = user_id)
        planner=User.objects.get(id=user_id)
        Trip.objects.create(destination=destination, plan=plan, start=start, end=end, planner=planner)
        return redirect('/dashboard')
def join(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    user_id=request.session['id']
    joiner = User.objects.get(id=user_id)
    Join.objects.create(trip = trip, joiner = joiner)
    return redirect('/dashboard')
def show(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    joins = Join.objects.filter(trip=trip)
    context = {
        'trip': trip,
        'joins': joins,
    }
    return render(request, 'thing/trip.html', context)