from students import students
from utils import helpers

def app():
    helpers.add_student(students, "Praises", 30)
    highest_score = helpers.highest_score(students)
    lowest_score = helpers.lowest_score(students)
    average_score = helpers.average_score(students)

    print("The highest score is", highest_score, "\n")
    print("The lowest score is", lowest_score, "\n")
    print("The average score is", average_score, "\n")
    print("The logged students: ", students, "\n")


if __name__ == '__main__':
    print("Starting app....")
    app()