from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.crud import (
    get_books,
    create_book,
    update_book,
    delete_book
)
from app.schemas import (
    BookCreate,
    BookResponse
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get("/", response_model=list[BookResponse])
def read_books(
    db: Session = Depends(get_db)
):
    return get_books(db)


@router.post("/", response_model=BookResponse)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return create_book(
        db,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )


@router.put("/{book_id}")
def edit_book(
    book_id: int,
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return update_book(
        db,
        book_id,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )


@router.delete("/{book_id}")
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return delete_book(
        db,
        book_id
    )