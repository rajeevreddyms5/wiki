from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Visiting /wiki/TITLE render a page that displays the contents of that encyclopedia entry.
def view_entry(request, name):
        if util.get_entry(name):
            line1 = util.get_entry(name).split("\n")[0]
            title = line1.split(" ")[1]
            return HttpResponse(f"<title>{title}</title>{util.get_entry(name)}")
        else:
            return HttpResponseNotFound("<h1>Requested page was not found</h1>")

#search function    
def search_view(request):
    query_data = request.GET
    query = query_data.get('q')
    if util.get_entry(query) == None:
         return render(request, "encyclopedia/search.html", {
            "search_entries": util.search_entries(query)
        })
    else:
         return view_entry(request, query)
