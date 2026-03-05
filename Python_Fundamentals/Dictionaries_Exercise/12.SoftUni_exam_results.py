user_points = {}
submissions = {}
while True:
    current_result = input().split("-")
    # Case where we have 'exam finished'
    if len(current_result) == 1:
        break
    # Case where someone is banned
    elif len(current_result) == 2:
        user = current_result[0]
        del user_points[user]
    # Case where we have submission
    else:
        name, course, points = \
            current_result[0], current_result[1], int(current_result[2])
        if name not in user_points.keys():
            user_points[name] = 0
        if points > user_points[name]:
            user_points[name] = points
        if course not in submissions.keys():
            submissions[course] = 0
        submissions[course] += 1
print("Results:")
for name, points in user_points.items():
    print(f"{name} | {points}")
print("Submissions:")
for course, number_of_submissions in submissions.items():
    print(f"{course} - {number_of_submissions}")