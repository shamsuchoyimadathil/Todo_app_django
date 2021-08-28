from django.shortcuts import render

from . import forms 

#for main page , 
def index(request):
    context = {}
    form = forms.MainForm(request.POST)
    if form.is_valid():
        form.save() 
    
    context['form'] = form 


    return render (request,"index.html",context)