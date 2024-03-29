
from django.urls import path

from . import views

urlpatterns = [
    path('add_book/',views.add_book ),
    path('view_book/',views.view_all_books,name='view_book' ),

  
]
