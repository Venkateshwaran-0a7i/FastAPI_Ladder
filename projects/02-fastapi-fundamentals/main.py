from typing import List

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Fundamentals Project")


class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    price: float
    in_stock: bool = True


class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True


items_db: List[Item] = [
    Item(id=1, name="Laptop", price=1200.0, in_stock=True),
    Item(id=2, name="Mouse", price=25.0, in_stock=False),
]


@app.get("/")
def home() -> dict:
    return {"message": "Welcome to the FastAPI learning app"}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/items", response_model=List[Item])
def get_items() -> List[Item]:
    return items_db


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate) -> Item:
    new_item = Item(id=len(items_db) + 1, **item.model_dump())
    items_db.append(new_item)
    return new_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate) -> Item:
    for index, current in enumerate(items_db):
        if current.id == item_id:
            updated = Item(id=item_id, **item.model_dump())
            items_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    for index, current in enumerate(items_db):
        if current.id == item_id:
            del items_db[index]
            return
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/search")
def search_items(q: str = Query(..., min_length=1), limit: int = 5) -> dict:
    matches = [item for item in items_db if q.lower() in item.name.lower()]
    return {"query": q, "limit": limit, "items": matches[:limit]}
