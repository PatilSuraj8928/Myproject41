from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class StudentFormview(FormView):
    template_name='StudentForm.html'
    form_class=StudentForm

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))

class BheemaGFview(FormView):
    template_name='BheemaGF.html'
    form_class=BheemaGFForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data submitted successfully!!')