line = input().split()
stock = {}

for i in range(0, len(line), 2):
    stock[line[i]] = int(line[i + 1])

products_to_search = input().split()

for product in products_to_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")