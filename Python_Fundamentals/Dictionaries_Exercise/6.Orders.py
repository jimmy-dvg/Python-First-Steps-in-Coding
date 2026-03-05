products = {}

while True:
    line = input()
    if line == "buy":
        break

    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price  # replace price if different

for name, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{name} -> {total_price:.2f}")