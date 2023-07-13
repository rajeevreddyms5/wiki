from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Visiting /wiki/TITLE render a page that displays the contents of that encyclopedia entry.
def view_entry(request, name):
        if util.get_entry(name):
            return render(request, "encyclopedia/viewpage.html", {
                 "name": name,
                 "view": markdown2.markdown(util.get_entry(name))
            })
        else:
            return render(request, "encyclopedia/viewpage.html", {
                 "name": name,
                 "view": f"{name} page not found"
            })

#search function    
def search_view(request):
    query_data = request.GET
    query = query_data.get('q')
    if util.get_entry(query) == None:
        if len(util.search_entries(query)) == 0:
             return view_entry(request, query) 
        else:
            return render(request, "encyclopedia/search.html", {
                "search_entries": util.search_entries(query)
            })
    else:
         return view_entry(request, query)
     

#create new page entry function
def new_page(request):
    return render(request, "encyclopedia/newpage.html")


#save page function for view page
def save_page(request):
    query_data = request.POST
    title = query_data.get('title')
    temp = query_data.get('content')
    content = f"# {title}\n\n" + temp
    if util.get_entry(title):
            return render(request, "encyclopedia/viewpage.html", {
                 "name": title,
                 "view": f"<h1>ERROR - Encyclopedia entry of {title} already exists</h1>"
            })
    else:
        util.save_entry(title, content)
        return view_entry(request, title)
    

#edit page function
def edit_page(request):
    query_data = request.POST
    title = query_data.get('edit')
    return render(request, "encyclopedia/editpage.html", {
        "name": title,
        "view": util.get_entry(title)
    })


#save page function for edit page
def save_edited_page(request):
    query_data = request.POST
    title = query_data.get('title')
    content = query_data.get('content')
    util.save_entry(title, content)
    return view_entry(request, title)


# random page function
def random_page(request):
    title = util.random()
    return view_entry(request, title)