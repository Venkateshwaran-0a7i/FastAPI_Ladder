from fastapi import FastAPI
import calculator

app=FastAPI()

@app.post("/add")
def add_numbers(a: int, b: int):
    result = calculator.add(a, b)
    return {"result": result}

@app.post("/subtract")
def subtract_numbers(a: int, b: int):
    result = calculator.subtract(a, b)
    return {"result": result}

@app.post("/multiply")
def multiply_numbers(a: int, b: int):
    result = calculator.multiply(a, b)
    return {"result": result}

@app.post("/divide")
def divide_numbers(a: int, b: int):
    result = calculator.divide(a, b)
    return {"result": result}