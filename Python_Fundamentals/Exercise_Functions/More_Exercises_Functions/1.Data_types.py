def process_data():
    data_type = input()
    value = input()

    if data_type == "int":
        result = int(value) * 2
        print(result)
    elif data_type == "real":
        result = float(value) * 1.5
        print(f"{result:.2f}")
    elif data_type == "string":
        result = f"${value}$"
        print(result)


process_data()