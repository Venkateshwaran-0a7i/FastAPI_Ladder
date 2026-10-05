from fastapi import FastAPI

app = FastAPI()


@app.get("/greet")
def greet():
    return {"message": "Hello, welcome to the FastAPI application!"}




