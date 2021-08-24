from django.contrib import admin
from django.urls import path

from books.views import (
    create_book,
    create_book_form,
    detail_book,
    update_book,
    delete_book
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/', create_book, name='create-book'),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    path('htmx/book/<pk>/update/', update_book, name="update-book"),
    path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
]
