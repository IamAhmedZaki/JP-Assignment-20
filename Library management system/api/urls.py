from django.urls import path
from api import views

urlpatterns=[
    path('authors/',views.author_get_post),
    path('authors/<id>/',views.author_update_delete_get),
    path('genres/',views.Genre_get_post),
    path('genres/<id>/',views.Genre_update_delete_get),
    path('books/',views.book_get_post),
    path('books/<id>/',views.Book_update_delete_get)

    
]