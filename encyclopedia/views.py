from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view(request, name):
    if util.get_entry(name):
        line1 = util.get_entry(name).split("\n")[0]
        title = line1.split(" ")[1]
        return HttpResponse(f"<title>{title}</title> {util.get_entry(name)}")
    else:
        return HttpResponse("<h1>Requested page was not found</h1>")