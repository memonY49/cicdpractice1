from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student API")


class Student(BaseModel):
    name: str
    marks: float


@app.get("/")
def home():
    return {"message": "FastAPI CI/CD is working now!"}


@app.post("/result")
def calculate_result(student: Student):
    status = "Pass" if student.marks >= 50 else "Fail"

    return {
        "name": student.name,
        "marks": student.marks,
        "status": status
    }
