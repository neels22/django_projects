from django.shortcuts import render

# Create your views here.


def view_all_books(req):
    return render(req,"view_book.html")

def add_book(req):
    return render(req,"add_book.html")