from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class newform(forms.Form):
    task=forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[] 
    return render(request,'tasks/index.html',{"tasks":request.session["tasks"]})

def addtask(request):     
    if(request.method=="POST"):
        form=newform(request.POST)
        if form.is_valid():
        
        #This statement get the specific field from the class form    
            task= form.cleaned_data["task"]
            request.session["tasks"]+=[task]
        
        # This Statement Redirects Http Response when you submit data    
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/addtask.hmtl",{
                "form":newform()
            })

    
    return render(request, "tasks/addtask.html",{
        "form":newform()
        })
#     if request.method=="POST"
#         form = newform(request.POST)
#         if form.is_valid():
#     task=form.cleaned_data["task"];
#     tasks.append(task);
#     # return HttpResponseRedirect(reverse("tasks:addtask"))
# else:
