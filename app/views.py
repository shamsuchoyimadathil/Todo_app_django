from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from . import forms 
from . import models

#for main page , 
def index(request):
    context = {}

    form = forms.MainForm(request.POST)
    alltasks = models.Main.objects.all()
    #deletetask = models.Main.objects.filter(pk=id).delete()


    if form.is_valid():
        cleaned_data = form.cleaned_data
        data = models.Main(title = cleaned_data['title'])
        data.save() 
        return HttpResponseRedirect('/')
    else:
        form = forms.MainForm()
    
    context['form'] = form 
    context['alltasks'] = alltasks 
    #context['deletetask'] = deletetask

    return render (request,"index.html",context)


def delete(request,id):
    delete_task = get_object_or_404(models.Main,pk=id).delete()
    return redirect("/")



# class DeleteTask(DeleteView):
#     model = models.Main 
#     template_name = "index.html"
#     success_url = "/"