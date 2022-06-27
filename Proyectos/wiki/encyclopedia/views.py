from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util


def index(request):
    if request.method == "POST":
       title = request.POST.get("q")
       entries = util.list_entries()
       new_entries = []
       for entry in entries:
           if title.upper() in entry.upper():
               new_entries.append(entry)
           if entry.upper() == title.upper():  
            return render(request, "encyclopedia/entrada.html", {
            "entrada": util.get_entry(title)
            })
       return render(request, "encyclopedia/index.html", {
            "entries": new_entries
            })
     

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
         })


def entrada(request, name):
    return render(request, "encyclopedia/entrada.html", {
        "entrada": util.get_entry(name)
    })

def newpage(request):
     return render(request, "encyclopedia/newpage.html", {
    })

def randompage(request):
    return HttpResponse("Hola")