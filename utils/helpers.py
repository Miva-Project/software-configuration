
def highest_score(students) -> int:
    highest_score = students[0]['score']
    for student in students:
        if student['score'] > highest_score:
            highest_score = student['score']
    
    return highest_score        
    

def lowest_score(students):
    lowest_score = students[0]['score']
    for student in students:
        if student['score'] < lowest_score:
            lowest_score = student['score']
    
    return lowest_score
    
def average_score(data):
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)

def add_student(data, name, score):
    data.append({"name": name, "score": score})
    

