"""
Lien : https://www.youtube.com/watch?v=tLKKmouUams
01:00:25

À saisir dans le terminal :
uvicorn main:app --reload

Date : 14-05-2024
"""
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}

@app.get("/")
def index() -> dict:
    return {"name": "First Data"}

# Get avec paramètre
@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        description="The ID of the student you want to view", # Titre
        gt=0, # valeur minimale supérieur à ...
        lt=2, # valeur maximale inférieure à
        )):
    return students[student_id]
# print(students[1])

# Get avec requête
# Optional : pas d'erreur si aucune saisie n'est faite
@app.get("/get-by-name/")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# Get avec combinaison paramètre ET requête
@app.get("/get-all/{student_id}")
def get_all(student_id: int=Path(
                description="The ID of the student you want to view",
                gt=0,
                lt=2),
            name: Optional[str]=None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

class Student(BaseModel):
    name: str
    age: int
    year: str
    
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    del students[student_id] 
    return {"Message": "Student deleted successfully"}
