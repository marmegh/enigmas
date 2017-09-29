# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors = {}
        #!!!!!Check if user already exists!!! By Email.
        emailsearch = User.objects.filter(email = postData['email'])
        if len(emailsearch)>0:
            errors['email'] = 'Account already exists'
        #!!!!!Check if user already exists!!! By Username.
        usersearch = User.objects.filter(username = postData['username'])
        if len(usersearch)>0:
            errors['username'] = 'Username already in use'
        #check if first name is at least one character long
        if len(postData['name'])<1:
            errors['name'] = "Name required"
        elif len(postData['name'])<3:
            errors['name'] = "Name too short"
        #check if last name is at least two characters long
        if len(postData['username'])<1:
            errors['username'] = "Username required"
        elif len(postData['username'])<2:
            errors['username'] = "Username too short"
        #check that passwords match
        if postData['pwd'] != postData['cpw']:
            errors['password'] = "Confirmation did not match password"
        if postData['pwd'] < 8:
            errors['password'] = "Passwords must be at least 8 characters long"
        return errors
    def login_validator(self,postData):
        errors = {}
        #check if user exists
        username = postData['username']
        usersearch = User.objects.filter(username = username)
        if len(usersearch) < 1:
            errors['username']='User not found'
        #verify password
        else:
            pwd = postData['pwd']
            temp = User.objects.get(username = username)
            hashedpw = temp.password
            if not bcrypt.checkpw(pwd.encode(), hashedpw.encode()):
                errors['password']='Unable to authenticate'
        return errors

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
