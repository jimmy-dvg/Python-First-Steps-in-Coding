# Read contests and passwords
contests = {}

while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

# Read submissions
users = {}

while True:
    line = input()
    if line == "end of submissions":
        break

    contest, password, username, points = line.split("=>")
    points = int(points)

    # Validate contest and password
    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        # Update points only if higher
        if contest not in users[username] or users[username][contest] < points:
            users[username][contest] = points

# Find best candidate
best_user = ""
best_total = 0

for user, contests_data in users.items():
    total = sum(contests_data.values())
    if total > best_total:
        best_total = total
        best_user = user

print(f"Best candidate is {best_user} with total {best_total} points.")
print("Ranking:")

# Print ranking
for user in sorted(users.keys()):
    print(user)
    # contests sorted by points descending
    for contest, pts in sorted(users[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {pts}")