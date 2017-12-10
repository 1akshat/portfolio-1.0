# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	subject = forms.CharField(max_length=100)
	message = forms.CharField()