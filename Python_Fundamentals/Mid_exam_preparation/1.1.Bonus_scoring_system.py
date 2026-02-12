number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_attendances = 0
total_bonus = 0
for current_student in range(number_of_students):
    attendance_of_current_student = int(input())
    if attendance_of_current_student > max_attendances:
        max_attendances = attendance_of_current_student
if number_of_lectures > 0:
    total_bonus = max_attendances / number_of_lectures * (5 + additional_bonus)
print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")