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


6. @app.get("/products")
def products(category: str):
    return {"category": category}

What do you think happens for these three requests?

A
/products?category=milk
    {"category":"milk"}

B
/products?category=juice
    {"category":"juice"}
C
/products
    errors 404


**Day 1 Final questions**

Absolutely. 😎 Here's your **Day 1 Final Challenge**.

Don't search for the answer. Use what you've learned.

# 🧪 FastAPI Day 1 Final Challenge

Imagine this is your `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome"}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}


@app.get("/products")
def get_products(category: str = "all"):
    return {"category": category}
```

## Part 1 — Predict the response

For each request, tell me:

**1.**

```text
GET /
```

What response? - {"message": "Welcome"}

---

**2.**

```text
GET /products/25
```

What response? - {"product_id": 25}

---

**3.**

```text
GET /products/abc
```

What happens? - 422 invalid error

---

**4.**

```text
GET /products
```

What response? - {"category":"all"} --

__Remember__

 /products
    ↓
Route exists
    ↓
category not provided
    ↓
default = "all"
    ↓
{"category": "all"}

**5.**

```text
GET /products?category=milk
```

What response? {"category": "milk"}

---

**6.**

```text
GET /unknown
```

What happens? - 404

---

# Part 2 — Explain the flow

For this request:

```text
GET /products/42
```

Explain the complete flow in your own words. 

Something like:

```text
Browser
   ↓
Requesting /product/25
   ↓
validate
   ↓
Return the product as reponce if the validation pass or else the validation failed 422
```

I want you to explain **what FastAPI does**, not just give the final response.

---

# Part 3 — Write your own endpoint

Create an endpoint for a user:

```text
GET /users/10
```

It should return:

```json
{
    "user_id": 10
}
```

Write the FastAPI code yourself.

@app.get("/users/{user_id}")
def user(user_id:int):
    return {"user_id":user_id}

---

# Part 4 — One conceptual question 🧠

Explain the difference between:

```text
/products/10
```

and

```text
/products?category=milk
```

In your own words.

The products/25 is the path and used to get the specific product detials but the query is different the ? is an seperator which seperate the path and query. the query is used to filter the products in category i want all products have milk 
---

### Your answer format

Reply like this:

````text
1. ...
2. ...
3. ...
4. ...
5. ...
6. ...

Flow:
...

Part 3:
```python
...
````

Part 4:
...

```

Take your time. **Don't worry about making mistakes.** I'm checking your understanding, not looking for perfect wording.

If you pass this, I'll check your **FastAPI_Ladder** repo one more time and we'll officially close **Day 1**. 🚀
```

**Part 1**
1. {"message": "Welcome"}
2. {"product_id": 25}
3. 422 invalid error
4. {"category":"all"}
5. {"category": "milk"}
6. 404

**Part -2**

Browser
   ↓
Requesting /product/25
   ↓
validate
   ↓
Return the product as reponce if the validation pass or else the validation failed 422

**Part -3**

@app.get("/users/{user_id}")
def user(user_id:int):
    return {"user_id":user_id}

**Part - 4**

The products/25 is the path and used to get the specific product detials but the query is different the ? is an seperator which seperate the path and query. the query is used to filter the products in category i want all products have milk 



**================ Day- 2 ==================**

@app.get("/products")
def get_products():
    return {"message": "Get products"}


@app.post("/products")
def create_product():
    return {"message": "Create product"}

What happens if:

A The browser requests:

GET /products - The request returns with the responce of products on DB 


B The client sends:

POST /products - Thats makes it as error if the url dosn't have the body what to create


C The browser requests:

DELETE /products - delete the product 



Which HTTP method?
    They are the methods to communicate with database and make changes in database

Which path?
    paths are the endpoints we created for the specific task or and functions

Path parameter or query parameter?
    Path parameter is used to veiw or do some opertions in DB at same time Query parameter is the additional option to filter the data we get and the ? is used for seperate the path and query

Request body or not?
    Request body is used for post and put methods along with path the body contain the values we want to create and update 

Which Pydantic model?
    we currently used basemodel the basemodel is the toolkits that gives class capabilities such as validations, typing check, passing income data

What happens when the data is invalid?
    id the data is invalid it return 422 error but we can manage the problem with try: exept(): methods