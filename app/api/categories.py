from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db.crud import (
    get_categories,
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
def read_categories(
    db: Session = Depends(get_db)
):
    return get_categories(db)


@router.post("/", response_model=CategoryResponse)
def add_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return create_category(
        db,
        category.title
    )


@router.put("/{category_id}")
def edit_category(
    category_id: int,
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return update_category(
        db,
        category_id,
        category.title
    )


@router.delete("/{category_id}")
def remove_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return delete_category(
        db,
        category_id
    )