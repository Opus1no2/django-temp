from django.core.management.base import BaseCommand, CommandError
from django.db import reset_queries
from django.db import connection
import pprint

from ...models import Book

pp = pprint.PrettyPrinter(indent=2)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        reset_queries()

        for book in Book.objects.all():
            book.author

        pp.pprint(connection.queries)
        pp.pprint("now with select related:")

        reset_queries()
        for book in Book.objects.all().select_related('author').all():
            book.author

        pp.pprint(connection.queries)
