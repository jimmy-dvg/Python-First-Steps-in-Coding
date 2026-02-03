city = input()
sales = float(input())
commision = -1

if city == "Sofia":
    if 0 <= sales <= 500:
        commision = 0.05
    elif 500 <= sales <= 1000:
        commision = 0.07
    elif 1000 <= sales <= 10000:
        commision = 0.08
    elif sales > 10000:
        commision = 0.12
if city == "Varna":
    if 0 <= sales <= 500:
        commision = 0.045
    elif 500 <= sales <= 1000:
        commision = 0.075
    elif 1000 <= sales <= 10000:
        commision = 0.10
    elif sales > 10000:
        commision = 0.13
if city == "Plovdiv":
    if 0 <= sales <= 500:
        commision = 0.055
    elif 500 <= sales <= 1000:
        commision = 0.08
    elif 1000 <= sales <= 10000:
        commision = 0.12
    elif sales > 10000:
        commision = 0.145

if commision >= 0:
    total = commision * sales
    print(f"{total:.2f}")
else:
    print("error")