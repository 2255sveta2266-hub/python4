from app.db.models import Category, Book

def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    return category

def get_categories(db):
    return db.query(Category).all()

def create_book(
    db,
    title,
    description,
    price,
    url,
    category_id
):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    db.add(book)
    db.commit()

    return book

def get_books(db):
    return db.query(Book).all()