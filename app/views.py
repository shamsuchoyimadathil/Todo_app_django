from django.shortcuts import render


#for main page , 
def index(request):

    return render (request,"index.html")