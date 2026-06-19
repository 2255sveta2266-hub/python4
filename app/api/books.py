from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.crud import (
    get_books,
    get_book_by_id,
    get_books_by_category,
    get_category_by_id,
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
    category_id: int | None = None,
    db: Session = Depends(get_db)
):
    if category_id:
        return get_books_by_category(
            db,
            category_id
        )

    return get_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def read_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = get_book_by_id(db, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    category = get_category_by_id(
        db,
        book.category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

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
    category = get_category_by_id(
        db,
        book.category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    result = update_book(
        db,
        book_id,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return result


@router.delete("/{book_id}")
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    result = delete_book(db, book_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {"message": "Book deleted"}