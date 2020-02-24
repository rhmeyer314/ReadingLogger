from django.db import models
from django.contrib.postgres.fields import ArrayField

class UserSelectedBookID(models.Model):
    username = models.CharField(max_length=20)
    book_id = models.CharField(max_length=30)
    book_title = models.CharField(max_length=100)
    authors = ArrayField(models.CharField(max_length=50))
    page_count = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('username', 'book_id')
