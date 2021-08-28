from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name="index"),
    #path("delete/<int:pk>",views.DeleteTask.as_view() , name="delete"),
    path("delete/<int:id>",views.delete,name="delete")
]
