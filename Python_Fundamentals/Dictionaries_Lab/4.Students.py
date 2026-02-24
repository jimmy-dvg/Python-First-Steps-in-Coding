students = {}

while True:
    line = input()
    if ":" not in line:
        course_filter = line
        break
    name, student_id, course = line.split(":")
    students[student_id] = {"name": name, "course": course}

for student_id, info in students.items():
    if info["course"] == course_filter:
        print(f"{info['name']} - {student_id}")