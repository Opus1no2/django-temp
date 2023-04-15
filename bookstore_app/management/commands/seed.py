from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from ...models import Book, Author
from datetime import date

fake = Faker()

class Command(BaseCommand):
    help = "seeds database"

    def handle(self, *args, **kwargs):
        print("clearing database...")

        Book.objects.all().delete()

        print("seeding database...")

        for _ in range(5):
            Book.objects.create(
                title=fake.text(max_nb_chars=20),
                published_at=date.today(),
                author=Author.objects.create(name=fake.name()))
