**============== Day 1 ============**

1. What is FastAPI?
    It is python framework which is used for building API

2. What does this do?

app = FastAPI()
    That repreasent the python FastAPI app is creating as app

3. What does this mean?

@app.get("/")
    It is the decorator and the GET request send to the app in the path of "/"

4. What does this function do?

def home():
    return {"message": "Hello"}
    this is an python fuction whenever the funtion get called by API the Code inside the function will be executed.
    here, the responce for this fuction is {"message":"Hello"}, the request for this path will respond with this return


5. What happens when you open:

http://127.0.0.1:8000/

it open the browser and show nothing but when i change or add the end point with the url the massege for the url will appear for example http://127.0.0.1:8000/about -> the responce will be {"name": "Venkat",
            "role":"AI Engineer"}