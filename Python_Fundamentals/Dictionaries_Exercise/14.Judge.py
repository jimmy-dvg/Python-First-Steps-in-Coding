contests = {}   # contest -> {user: points}
users = {}      # user -> {contest: points}

while True:
    line = input()
    if line == "no more time":
        break

    username, contest, points = line.split(" -> ")
    points = int(points)

    # Save in contests
    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points
    else:
        if contests[contest][username] < points:
            contests[contest][username] = points

    # Save in users
    if username not in users:
        users[username] = {}

    if contest not in users[username]:
        users[username][contest] = points
    else:
        if users[username][contest] < points:
            users[username][contest] = points

# Print contests in order of input
for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")

    sorted_participants = sorted(
        participants.items(),
        key=lambda x: (-x[1], x[0])
    )

    position = 1
    for user, pts in sorted_participants:
        print(f"{position}. {user} <::> {pts}")
        position += 1

# Individual standings
print("Individual standings:")

# Calculate total points
totals = {}
for user, contests_data in users.items():
    totals[user] = sum(contests_data.values())

sorted_totals = sorted(
    totals.items(),
    key=lambda x: (-x[1], x[0])
)

position = 1
for user, total in sorted_totals:
    print(f"{position}. {user} -> {total}")
    position += 1