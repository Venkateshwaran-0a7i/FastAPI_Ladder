# from fastapi import FastAPI
# import uvicorn

# from app import app

# @app.get("/greet")
# def greet():
#     return {"message": "Hello, welcome to the FastAPI application!"}



# if __name__ == "__main__":
#     uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)




from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about():
    return {"name": "Venkat",
            "role":"AI Engineer"}
