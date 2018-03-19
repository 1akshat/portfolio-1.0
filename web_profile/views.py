# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail

from django.shortcuts import render
from .models import EmailForm


def home(request):
	return render(request, 'index.html', {})


def sendmail(request):
	if request.method=="POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message + " from " + email, 'akshat.akshat6@gmail.com', ['akshatuppalweb@gmail.com'])
				return HttpResponseRedirect('/')
			except Exception as e:
				HttpResponse('t Block executed.' + str(e))
		else:
			return HttpResponse("Form not Valid")
	else:
		return HttpResponseRedirect('/')  
