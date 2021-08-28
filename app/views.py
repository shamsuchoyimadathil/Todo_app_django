from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import datetime

from . import forms 
from . import models

#for main page , 
def index(request):
    context = {}

    form = forms.MainForm(request.POST)
    alltasks = models.Main.objects.all()
    dateandtime = datetime.datetime.now()

    if form.is_valid():
        cleaned_data = form.cleaned_data
        data = models.Main(title = cleaned_data['title'])
        data.save() 
        return HttpResponseRedirect('/')
    else:
        form = forms.MainForm()
    
    context['form'] = form 
    context['alltasks'] = alltasks 
    context['dateandtime'] = dateandtime

    return render (request,"index.html",context)

#for deleting to do 
def delete(request,id):
    delete_task = get_object_or_404(models.Main,pk=id).delete()
    return redirect("/")