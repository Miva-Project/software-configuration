
def highest_score(students) -> int:
    if not students:
        return 0
    if len(students) == 0:
        return 0

    highest_score = students[0]['score']
    for student in students:
        if student['score'] > highest_score:
            highest_score = student['score']

    return highest_score


def lowest_score(students):
    if not students:
        return 0
    if len(students) == 0:
        return 0

    lowest_score = students[0]['score']
    for student in students:
        if student['score'] < lowest_score:
            lowest_score = student['score']

    return lowest_score

def average_score(students):
    if not students:
        return 0
    if len(students) == 0:
        return 0

    total = 0
    for d in students:
        total += d["score"]
    return total / len(students)

def add_student(students, name, score):

    students.append({"name": name, "score": score})
