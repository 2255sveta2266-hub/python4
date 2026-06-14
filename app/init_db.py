from app.db.db import engine, SessionLocal
from app.db.models import Base
from app.db.crud import (
    create_category,
    create_book
)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

cat1 = create_category(db, "Фантастика")
cat2 = create_category(db, "Программирование")

create_book(
    db,
    "Dune",
    "Фантастический роман",
    1000,
    "",
    cat1.id
)

create_book(
    db,
    "Foundation",
    "Книга Азимова",
    1200,
    "",
    cat1.id
)

create_book(
    db,
    "Python",
    "Изучение Python",
    1500,
    "",
    cat2.id
)

create_book(
    db,
    "SQL",
    "Работа с БД",
    900,
    "",
    cat2.id
)

print("Данные добавлены")