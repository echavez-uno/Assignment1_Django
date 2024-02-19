from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),

    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),

    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    # Added by me; Segment 5, step #32, 1) b.


    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    # Added by me; Segment 5, step #32, 2) c.
]

