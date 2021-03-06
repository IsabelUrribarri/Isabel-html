from email import message
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from markdown2 import Markdown
import html2markdown
import random
from . import util


def index(request):
    if request.method == "POST":
        title = request.POST.get("q")
        entries = util.list_entries()
        new_entries = []
        for entry in entries:
            if entry.upper() == title.upper():
                return render(request, "encyclopedia/entrada.html", {
                    "title" : title.upper(),
                    "entrada": util.get_entry(title)
                })
            if title.upper() in entry.upper():
                new_entries.append(entry)
        if new_entries :
            return render(request, "encyclopedia/index.html", {
                "entries": new_entries,
                "search" : True,
                "results": True
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "results": False,
                "search" : True,
                "entries": None
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
    error = False
    message = ""
    if request.method == "POST":
        data = request.POST.dict()
        title = data.get('title')
        description = data.get('description')
        print(util.get_entry(title))
        if title != "":
            if util.get_entry(title) is None:
                util.save_entry(title, description)
            else:
                error = True
                message = "This entry already exists"
        else:
            error = True
            message = "You must write a title"

    return render(request, "encyclopedia/newpage.html", {
        "error": error,
        "message": message
    })


def randompage(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return render(request, "encyclopedia/entrada.html", {
        "entrada": util.get_entry(entry),
        "title": entry.capitalize()
    })

def editpage(request,entry):
    if request.method == "POST":
        data = request.POST.dict()
        description = data.get('description')
        util.save_entry(entry, description)
        return render(request, "encyclopedia/entrada.html", {
        "entrada": util.get_entry(entry),
        "title": entry.capitalize()
    })
    else: 
        return render(request, "encyclopedia/editpage.html", {
            "entry": entry,
            "description": html2markdown.convert(util.get_entry(entry))
        })