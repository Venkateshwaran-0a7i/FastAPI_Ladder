from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

class responseModel(BaseModel):
    message: str
    product: Product

app = FastAPI()

products = {
    1: Product(id=1, name="Chocolate Milk", price=60),
    2: Product(id=2, name="Vanilla Milk", price=50),
    3: Product(id=3, name="Strawberry Milk", price=70),
    4: Product(id=4, name="Banana Milk", price=65)
}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]

@app.post("/products", status_code=201)
def create_product(product: Product):
    products[product.id] = product
    return responseModel(message="Product created successfully", product=product)
