def calculate_grade(name, marks):

    if marks >= 0 and marks <= 100:

        # Nested if
        if marks >= 50:

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            else:
                grade = "D"

            print("\nStudent Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)
            print("Result: Pass")

        else:
            print("\nStudent Name:", name)
            print("Marks:", marks)
            print("Grade: F")
            print("Result: Fail")

    else:
        print("Marks should be between 0 and 100.")


# Main program

student_name = input("Enter student name: ")

try:
    marks = int(input("Enter student marks: "))

    calculate_grade(student_name, marks)

except ValueError:
    print("Please enter a valid number for marks.")
