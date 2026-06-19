from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.crud import (
    get_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category
)
from app.schemas import (
    CategoryCreate,
    CategoryResponse
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/", response_model=list[CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return get_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED
)
def add_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return create_category(db, category.title)


@router.put("/{category_id}")
def edit_category(
    category_id: int,
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    result = update_category(
        db,
        category_id,
        category.title
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return result


@router.delete("/{category_id}")
def remove_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    result = delete_category(db, category_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {"message": "Category deleted"}