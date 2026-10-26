
from fastapi import FastAPI, Depends

app = FastAPI()


def pagination(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }


@app.get("/products")
def get_products(settings: dict = Depends(pagination)):
    return settings


@app.get("/orders")
def get_orders(settings: dict = Depends(pagination)):
    return settings

# ================== Mini Project  ==================

def common_parameters(name: str | None = None, limit: int = 10):
    return {"name": name, "limit": limit}


@app.get("/products")
def get_products(settings: dict = Depends(common_parameters)):
    return settings