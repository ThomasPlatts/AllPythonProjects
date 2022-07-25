import sys

grade_boundaries = [[], [], [], [], [], []]
grade_letters = ["A", "B", "C", "D", "E", "F"]
grade_list_index = 0
grade_letter_index = 0

student_marks = []

class_amount = int(input("How many students are in your class? "))
test_total = int(input("How many marks is the test out of? "))

test_total_check = test_total

for a in range(6):
    test_total -= 8
    grade_boundaries[grade_list_index].append(grade_letters[grade_letter_index])
    grade_boundaries[grade_list_index].append(test_total)
    grade_list_index += 1
    grade_letter_index += 1
print(f"Grade Boundaries are: {grade_boundaries}")

student_number = 1
for i in range(class_amount):
    test_marks = int(input(f"How many marks did student {student_number} get: "))
    if test_marks > test_total_check:
        print("Test marks cannot be higher than the test total... re-run the program")
        sys.exit()
    else:
        student_number += 1
        student_marks.append(test_marks)

student_marks_index = 0
student_ID = 1
for b in range(class_amount):
    if student_marks[student_marks_index] >= grade_boundaries[0][1]:
        print(f"Student number {student_ID} achieved a grade {grade_boundaries[0][0]}")
        student_ID += 1
        student_marks_index += 1
    elif grade_boundaries[0][1] > student_marks[student_marks_index] >= grade_boundaries[1][1]:
        print(f"Student number {student_ID} achieved a grade {grade_boundaries[1][0]}")
        student_ID += 1
        student_marks_index += 1
    elif grade_boundaries[1][1] > student_marks[student_marks_index] >= grade_boundaries[2][1]:
        print(f"Student number {student_ID} achieved a grade {grade_boundaries[2][0]}")
        student_ID += 1
        student_marks_index += 1
    elif grade_boundaries[2][1] > student_marks[student_marks_index] >= grade_boundaries[3][1]:
        print(f"Student number {student_ID} achieved a grade {grade_boundaries[3][0]}")
        student_ID += 1
        student_marks_index += 1
    elif grade_boundaries[3][1] > student_marks[student_marks_index] >= grade_boundaries[4][1]:
        print(f"Student number {student_ID} achieved a grade {grade_boundaries[4][0]}")
        student_ID += 1
        student_marks_index += 1
    elif grade_boundaries[4][1] > student_marks[student_marks_index] >= grade_boundaries[5][1]:
        print(f"Student number {student_ID} achieved a grade {grade_boundaries[5][0]}")
        student_ID += 1
        student_marks_index += 1
    elif grade_boundaries[5][1] > student_marks[student_marks_index]:
        print(f"Student number {student_ID} achieved a grade U")
        student_ID += 1
        student_marks_index += 1
