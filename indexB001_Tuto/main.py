"""
Lien : https://www.youtube.com/watch?v=XnYYwcOfcn8&list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p&index=1
Cours : Fast API Tutorial, Part 1: Introduction

À saisir dans le terminal pour lancer FastApi :
uvicorn main:app --reload

Date : 27-05-2024
"""

from fastapi import FastAPI

# Instanciation de la librairie
app = FastAPI()

@app.get("/", description="This is our first route!")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}
