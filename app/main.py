from fastapi import FastAPI

from app.api.books import router as books_router
from app.api.categories import router as categories_router

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(books_router)
app.include_router(categories_router)