from pydantic import BaseModel, Field, ValidationError
from statistics import mean, median
from typing import List


class Student(BaseModel):
    name: str = Field(..., min_length=1)
    score: float = Field(..., ge=0)


def highest_score(students: List[Student]) -> float:
    print(students)
    if not students:
        return 0
    return max(s.score for s in students)


def lowest_score(students: List[Student]) -> float:
    if not students:
        return 0
    return min(s.score for s in students)


def average_score(students: List[Student]) -> float:
    if not students:
        return 0
    return mean(s.score for s in students)


def median_score(students: List[Student]) -> float:
    if not students:
        return 0
    return median(s.score for s in students)



def add_student(students_list: List[Student], name: str, score: float):
    try:
        student = Student(name=name, score=score)
        students_list.append(student)
    except ValidationError as e:
        print(e)
