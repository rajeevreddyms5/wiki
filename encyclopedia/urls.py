from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.view_entry, name="view_entry"),
    path("search/", views.search_view, name="search_view")
]
