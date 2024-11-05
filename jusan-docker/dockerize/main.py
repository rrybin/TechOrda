from fastapi import FastAPI, Header, Response, status
from typing import Union
from pydantic import BaseModel
import re

app = FastAPI()
result = []


class Elem(BaseModel):
    element: str


class expresion(BaseModel):
    expr: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sum1n/{number}")
def sum1n(number):
    result = sum(i for i in range(int(number) + 1))
    return {"result": result}


# 0 1 1 2 3
@app.get("/fibo")
def fibo(n: int):
    count = 1
    n1, n2 = 0, 1
    while count < n - 1:
        fib = n1 + n2
        n1, n2 = n2, fib
        count += 1
    return {"result": fib}


@app.post("/reverse")
def reverse(string: Union[str, None] = Header(default=None)):
    return {"result": string[::-1]}


@app.put("/list")
def add_to_list(element: Elem):
    result.append(element.element)


@app.get("/list")
def otput_list():
    return {"result:": result}


@app.post("/calculator", description="Sample: 1,+,1", status_code=200)
def calculator(expresion: expresion, response: Response):
    templ = re.compile(r"^\d*,[\+\-\*\/],\d*$")
    if not templ.fullmatch(expresion.expr):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error:": "invalid"}
    rest = expresion.expr.split(sep=',')
    if rest[1] == "+":
        return {"result": int(rest[0]) + int(rest[2])}
    elif rest[1] == "-":
        return {"result": int(rest[0]) - int(rest[2])}
    elif rest[1] == "*":
        return {"result": int(rest[0]) * int(rest[2])}
    elif rest[1] == "/":
        try:
            return {"result": int(rest[0]) / int(rest[2])}
        except:
            response.status_code = status.HTTP_403_FORBIDDEN
            return {"result": "zerodiv"}
