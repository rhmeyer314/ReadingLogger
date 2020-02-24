from django.shortcuts import render, redirect
from .models import UserSelectedBookID

import requests
from datetime import datetime
from .data import Data




def search(request):
    if (request.user.is_authenticated):
        return render(request, 'bookdata/search.html')
    else:
        return redirect('login')


def index(request):
    year = datetime.today().year
    data = Data()
    username = request.user.username

    year_book_count = data.year_book_count(username)
    year_page_count = data.year_page_count(username)
    year_unique_authors = data.year_unique_authors(username)
    month_book_count = data.month_book_count(username)
    month_page_count = data.month_page_count(username)
    month_unique_authors = data.month_unique_authors(username)

    if (request.user.is_authenticated):
        return render(request, 'bookdata/index.html', {
            'year_book_count': year_book_count,
            'year_page_count': year_page_count,
            'year_unique_authors': year_unique_authors,
            'month_book_count': month_book_count,
            'month_page_count': month_page_count,
            'month_unique_authors': month_unique_authors,
            'year': year,
        })
    else:
        return redirect('login')


def get_values(request):
    book_ids = request.POST.getlist('bookid')
    today = datetime.today()

    for book_id in book_ids:
        bookRequest = requests.get("https://www.googleapis.com/books/v1/volumes/" + book_id)
        book = bookRequest.json()

        book_title = book["volumeInfo"]["title"]
        page_count = book["volumeInfo"]["pageCount"]
        authors = book["volumeInfo"]["authors"]

        selected = UserSelectedBookID.objects.create(
            username=request.user.username,
            book_id=book_id,
            book_title=book_title,
            authors=authors,
            page_count=page_count,
            date=today.date(),
        )
        selected.save()
    return redirect('success')


def success(request):
    if (request.user.is_authenticated):
        return render(request, 'bookdata/success.html')
    else:
        return redirect('login')


def users_books(request):
    username = request.user.username
    data = Data()
    book_info = data.show_books(username)

    return render(request, 'bookdata/usersBooks.html', {'book_info': book_info})