from app.db.db import SessionLocal
from app.db.crud import (
    get_categories,
    get_books,
    update_category,
    update_book,
    delete_book
)

db = SessionLocal()

print("Категории ДО изменения:")

for category in get_categories(db):
    print(category.id, category.title)

print("\nКниги ДО изменения:")

for book in get_books(db):
    print(book.id, book.title, book.price)


# UPDATE

update_category(db, 1, "Научная фантастика")

update_book(
    db,
    1,
    "Dune (обновлено)",
    "Обновленное описание",
    2000,
    "",
    1
)

print("\nПосле UPDATE:")

for category in get_categories(db):
    print(category.id, category.title)

for book in get_books(db):
    print(book.id, book.title, book.price)


# DELETE

delete_book(db, 4)

print("\nПосле DELETE:")

for book in get_books(db):
    print(book.id, book.title, book.price)