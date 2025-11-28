from students import students
from utils import helpers


def app():

    helpers.add_student(students, "Blessing", 20)
    helpers.add_student(students, "Praises", 30)

    highest_score = helpers.highest_score(students)
    lowest_score = helpers.lowest_score(students)
    average_score = helpers.average_score(students)


    # ------ Student List Output ------
    print("\n==============================")
    print("REGISTERED STUDENTS")
    print("==============================")

    if not students:
        print("No students registered.")
    else:
        # Print a table header
        print(f"{'Name':<15} {'Score':<10}")
        print("-" * 25)

        # Print each student in the table
        for s in students:
            print(f"{s.name:<15} {s.score:<10}")

    # ------ Stats Summary ------
    print("\n==============================")
    print("SCORE SUMMARY")
    print("==============================")
    print(f"Highest Score : {highest_score}")
    print(f"Lowest Score  : {lowest_score}")
    print(f"Average Score : {average_score:.2f}")
    print("==============================\n")


if __name__ == '__main__':
    print("Starting app....\n")
    app()
