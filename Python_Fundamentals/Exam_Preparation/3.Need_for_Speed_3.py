n = int(input())
cars = {}

# Read cars
for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {
        "mileage": int(mileage),
        "fuel": int(fuel)
    }

while True:
    command = input()

    if command == "Stop":
        break

    parts = command.split(" : ")
    action = parts[0]
    car = parts[1]

    match action:

        case "Drive":
            distance = int(parts[2])
            fuel_needed = int(parts[3])

            if cars[car]["fuel"] < fuel_needed:
                print("Not enough fuel to make that ride")
            else:
                cars[car]["fuel"] -= fuel_needed
                cars[car]["mileage"] += distance

                print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

                if cars[car]["mileage"] >= 100000:
                    print(f"Time to sell the {car}!")
                    del cars[car]

        case "Refuel":
            fuel = int(parts[2])
            current_fuel = cars[car]["fuel"]

            fuel_added = min(fuel, 75 - current_fuel)
            cars[car]["fuel"] += fuel_added

            print(f"{car} refueled with {fuel_added} liters")

        case "Revert":
            kilometers = int(parts[2])
            cars[car]["mileage"] -= kilometers

            if cars[car]["mileage"] < 10000:
                cars[car]["mileage"] = 10000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")

# Final result
for car, data in cars.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")