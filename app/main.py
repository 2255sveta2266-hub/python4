from app.db.db import SessionLocal
from app.db.crud import (
    get_categories,
    get_books
)

db = SessionLocal()

print("Категории:")

for category in get_categories(db):
    print(category.id, category.title)

print("\nКниги:")

for book in get_books(db):
    print(
        book.id,
        book.title,
        book.price
    )