from fastapi import APIRouter

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/")
def get_categories():
    return [
        {"id": 1, "title": "Фантастика"},
        {"id": 2, "title": "Программирование"}
    ]