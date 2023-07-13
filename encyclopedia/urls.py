from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:name>", views.view_entry, name="view_entry"),
    path("search/", views.search_view, name="search_view"),
    path("newpage/", views.new_page, name="new_page"),
    path("save/", views.save_page, name="save_page"),
    path("edit/", views.edit_page, name="edit_page"),
    path("save_edited_page", views.save_edited_page, name="save_edited_page"),
    path("random/", views.random_page, name="random_page" )
]
