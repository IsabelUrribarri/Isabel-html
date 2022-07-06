from turtle import title
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
        "entrada": util.get_entry(name),
        "title": name.capitalize()
    })


def newpage(request):
    if request.method == "POST":
        data = request.POST.dict()
        title = data.get('title')
        description = data.get('description')
        print(util.get_entry(title))
        if title != "":
            if util.get_entry(title) is None:
                util.save_entry(title, description)
            else:
                return HttpResponse("This entry already exists")
        # else:
        #  return HttpResponse("You must include a title")

        return render(request, "encyclopedia/newpage.html", {
        })
    else:
        return render(request, "encyclopedia/newpage.html", {
        })


def randompage(request):
    return HttpResponse("Hola")


def editpage(request,entry):
    return HttpResponse("Edit page")