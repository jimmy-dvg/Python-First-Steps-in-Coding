budget = float(input())
season = input()

destination = ""
vacation_type = ""
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = budget * 0.30
        vacation_type = "Camp"
    else:
        spent = budget * 0.70
        vacation_type = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = budget * 0.40
        vacation_type = "Camp"
    else:
        spent = budget * 0.80
        vacation_type = "Hotel"

else:
    destination = "Europe"
    spent = budget * 0.90
    vacation_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {spent:.2f}")
