from django.urls import path

from . import views

app_name = "lms"
urlpatterns = [
    path("", views.index, name="index"),
    path("book/add/", views.add_book, name="add-book"),
    path("book/view/<str:book_id>/", views.view_book, name="view-book"),
    path("book/update/<str:book_id>/", views.update_book, name="update-book"),
    path("book/edit-category/", views.edit_category, name="edit-category"),
    path("book/edit-author/", views.edit_author, name="edit-author"),
    path("book/archive/<str:book_id>/", views.archive_book, name="archive-book"),
]
