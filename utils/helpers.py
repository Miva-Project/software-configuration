from pydantic import BaseModel, Field, ValidationError
from statistics import mean, median
from typing import List


class Student(BaseModel):
    """
    Represents a student with a validated name and score.

    Attributes:
        name (str): The student's name. Must be a non-empty string.
        score (float): The student's score. Must be a number >= 0.
    """
    name: str = Field(..., min_length=1)
    score: float = Field(..., ge=0)


def highest_score(students: List[Student]) -> float:
    """
    Returns the highest score among all students.

    Parameters:
        students (List[Student]): A list of Student objects.

    Default / Base Behavior:
        - If the list is empty, the function returns 0.

    Returns:
        float: The highest score found in the list, or 0 if empty.
    """
    if not students:
        return 0
    return max(s.score for s in students)


def lowest_score(students: List[Student]) -> float:
    """
    Returns the lowest score among all students.

    Parameters:
        students (List[Student]): A list of Student objects.

    Default / Base Behavior:
        - If the list is empty, the function returns 0.

    Returns:
        float: The lowest score found in the list, or 0 if empty.
    """
    if not students:
        return 0
    return min(s.score for s in students)


def average_score(students: List[Student]) -> float:
    """
    Calculates and returns the average score of all students.

    Parameters:
        students (List[Student]): A list of Student objects.

    Default / Base Behavior:
        - If the list is empty, the function returns 0.

    Returns:
        float: The average score, or 0 if the list is empty.
    """
    if not students:
        return 0
    return mean(s.score for s in students)


def median_score(students: List[Student]) -> float:
    """
    Calculates and returns the median score of all students.

    Parameters:
        students (List[Student]): A list of Student objects.

    Default / Base Behavior:
        - If the list is empty, the function returns 0.

    Returns:
        float: The median score value, or 0 if empty.
    """
    if not students:
        return 0
    return median(s.score for s in students)


def add_student(students_list: List[Student], name: str, score: float):
    """
    Creates and adds a new Student object to the students list with validation.

    Parameters:
        students_list (List[Student]): The list to append the new student to.
        name (str): The student's name.
        score (float): The student's score.

    Default / Base Behavior:
        - If the input is invalid (e.g., empty name, negative score),
          Pydantic raises a ValidationError, which is caught and printed.

    Returns:
        None: The function modifies the list in-place.
    """
    try:
        student = Student(name=name, score=score)  # Validation occurs here
        students_list.append(student)              # Add the validated student
    except ValidationError as e:
        print("Validation Error:\n", e)
