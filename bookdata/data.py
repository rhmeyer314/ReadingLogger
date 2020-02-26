from .models import UserSelectedBookID
from datetime import datetime

# Data class that deals with logic for the bookdata/views.py file
class Data:
    year = datetime.today().year
    month = datetime.today().month

    # gets page_count from specific user for current year and increments them all together. Returns sum of all pages
    def year_page_count(self, username):
        page_count = 0
        query = UserSelectedBookID.objects.filter(username=username, date__year=self.year).values('page_count')

        for pages in query:
            page_count += pages['page_count']

        return page_count

    # gets the total number of books from a specific user for current year. Returns the total number of books a user has read
    def year_book_count(self, username):
        query = UserSelectedBookID.objects.filter(username=username, date__year=self.year).values('id')

        return len(query)

    # gets the number of unique authors a user has read from this current year
    def year_unique_authors(self, username):
        unique_authors = set()
        query = UserSelectedBookID.objects.filter(username=username, date__year=self.year).values('authors')

        for authors in query:
            unique_authors.update(authors['authors'])

        return len(unique_authors)

    # gets page_count from specific user for current month and increments them all together. Returns sum of all pages
    def month_page_count(self, username):
        page_count = 0
        query = UserSelectedBookID.objects.filter(username=username, date__month=self.month, date__year=self.year).values('page_count')

        for pages in query:
            page_count += pages['page_count']

        return page_count

    # gets book_count from specific user for current month and increments them all together. Returns the total number of books a user has read
    def month_book_count(self, username):
        query = UserSelectedBookID.objects.filter(username=username, date__month=self.month, date__year=self.year).values('id')

        return len(query)

    # gets the number of unique authors a user has read from this current year
    def month_unique_authors(self, username):
        unique_authors = set()
        query = UserSelectedBookID.objects.filter(username=username, date__month=self.month, date__year=self.year).values('authors')

        for authors in query:
            unique_authors.update(authors['authors'])

        return len(unique_authors)

    # gets all books and their authors/page_count from a specific user.
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

