from .models import UserSelectedBookID
import requests
import json
from datetime import datetime

# Data class that deals with logic for the bookdata/views.py file
class Data:
    year = datetime.today().year
    month = datetime.today().month

    def year_page_count(self, username):
        page_count = 0
        query = UserSelectedBookID.objects.filter(username=username, date__year=self.year).values('page_count')

        for pages in query:
            page_count += pages['page_count']

        return page_count

    def year_book_count(self, username):
        query = UserSelectedBookID.objects.filter(username=username, date__year=self.year).values('id')

        return len(query)

    def year_unique_authors(self, username):
        unique_authors = set()
        query = UserSelectedBookID.objects.filter(username=username, date__year=self.year).values('authors')

        for authors in query:
            unique_authors.update(authors['authors'])

        return len(unique_authors)

    def month_page_count(self, username):
        page_count = 0
        query = UserSelectedBookID.objects.filter(username=username, date__month=self.month, date__year=self.year).values('page_count')

        for pages in query:
            page_count += pages['page_count']

        return page_count

    def month_book_count(self, username):
        query = UserSelectedBookID.objects.filter(username=username, date__month=self.month, date__year=self.year).values('id')

        return len(query)

    def month_unique_authors(self, username):
        unique_authors = set()
        query = UserSelectedBookID.objects.filter(username=username, date__month=self.month, date__year=self.year).values('authors')

        for authors in query:
            unique_authors.update(authors['authors'])

        return len(unique_authors)

    def show_books(self, username):
        book_info = []
        query = UserSelectedBookID.objects.filter(username=username).values('book_title', 'authors', 'page_count')

        for books in query:
            book_dict = {
                'book_title': books['book_title'],
                'authors': books['authors'],
                'page_count': books['page_count']
            }
            book_info.append(book_dict)

        return book_info

