
# 🧩 Day 2 Mini Project — Product API
# Goal
# Build a small Product Management API using FastAPI.
# You are building the backend for a simple product catalog. The API should allow a client to view, create, update, and delete products.


from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()  

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str

@app.get("/products")
def get_all_products():
    return [
        Product(id=1, name="Product 1", price=10.99, category="Category A"),
        Product(id=2, name="Product 2", price=15.49, category="Category B"),
        Product(id=3, name="Product 3", price=7.99, category="Category A"),
    ]

@app.get("/products/{id}")
def get_product(id: int):
    for product in get_all_products():
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    return {"message": "Product created successfully", "product": product}

@app.put("/products/{id}")
def update_product(id: int, updated_product: Product):
    for product in get_all_products():
        if product.id == id:
            return {"message": "Product updated successfully", "product": updated_product}
    return {"message": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int):
    for product in get_all_products():
        if product.id == id:
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)