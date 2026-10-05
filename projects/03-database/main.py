from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Database Project")


class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2)
    price: float
    category: str = "general"


products_db: List[Product] = [
    Product(id=1, name="Keyboard", price=49.99, category="tech"),
    Product(id=2, name="Desk lamp", price=19.99, category="home"),
]


@app.get("/products", response_model=List[Product])
def list_products() -> List[Product]:
    return products_db


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product) -> Product:
    product.id = (products_db[-1].id + 1) if products_db else 1
    products_db.append(product)
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product) -> Product:
    for index, current in enumerate(products_db):
        if current.id == product_id:
            product.id = product_id
            products_db[index] = product
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int) -> None:
    for index, current in enumerate(products_db):
        if current.id == product_id:
            del products_db[index]
            return
    raise HTTPException(status_code=404, detail="Product not found")


# Notes for real database integration:
# - Replace the in-memory list with MongoDB PyMongo/Beanie or SQLAlchemy models.
# - Use CRUD functions to separate database logic from route logic.
