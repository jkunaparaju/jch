
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from reg.models import  Registration


class RegistrationList(ListView):
    model = Registration


class RegistrationCreate(CreateView):
    model = Registration
    success_url = reverse_lazy('registration_list')

    fields = ['registrationnumber','firstname','lastname', 'phone','emergencyphone','street_address','citystatezip',
    'classnumber','attendance','memberid','receipt','fee','date', 'user', 'sex','zip','state','dob' ]




class RegistrationUpdate(UpdateView):
    model = Registration
    success_url = reverse_lazy('registration_list')
    fields = ['registrationnumber','firstname','lastname', 'phone','emergencyphone','street_address','citystatezip',
    'classnumber','attendance','memberid','receipt','fee','date', 'user', 'sex','zip','state','dob' ]


class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy('registration_list')