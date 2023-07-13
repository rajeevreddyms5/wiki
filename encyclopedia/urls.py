from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:name>", views.view_entry, name="view_entry"),
    path("search/", views.search_view, name="search_view"),
    path("newpage/", views.new_page, name="new_page"),
    path("save/", views.save_page, name="save_page")
]
