from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

class ResponseModel(BaseModel):
    message: str
    product: Product

app = FastAPI()

products = {
    1: Product(id=1, name="Chocolate Milk", price=60),
    2: Product(id=2, name="Vanilla Milk", price=50),
    3: Product(id=3, name="Strawberry Milk", price=70),
    4: Product(id=4, name="Banana Milk", price=65)
}

@app.get(
    "/products/{product_id}",
    response_model=Product
)
def get_product(product_id: int):
    # Keep your existing function body
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]

# @app.post(
#     "/products",
#     status_code=201,
#     response_model=ResponseModel
# )
# def create_product(product: Product):
#     # Keep your existing function body,
#     # but return ResponseModel(...) with the new class name
#     if product.id in products:
#         raise HTTPException (
#     status_code=409,
#     detail="Product ID already exists"
#     )
#     products[product.id] = product
#     return ResponseModel(message="Product created successfully", product=product)



@app.post(
    "/products",
    status_code=201,
    response_model=ResponseModel
)
def create_product(product: Product):
    if product.id in products:
        raise HTTPException(
            status_code=409,
            detail="Product ID already exists"
        )

    products[product.id] = product

    return ResponseModel(
        message="Product created successfully",
        product=product
    )

@app.put("/products/{product_id}", response_model=ResponseModel)
def update_products(product_id: int, updated_product: Product):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    products[product_id] = updated_product

    return ResponseModel(
        message="Product updated successfully",
        product=updated_product
    )