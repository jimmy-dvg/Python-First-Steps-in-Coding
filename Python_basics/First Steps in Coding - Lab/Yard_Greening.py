sq_m = float(input())

price_per_sq_m = 7.61
discount = 0.18

cost_without_discount = sq_m * price_per_sq_m
discount_amount = cost_without_discount * discount

final_cost = cost_without_discount - discount_amount

print(f"The final price is: {final_cost} lv.")
print(f"The discount is: {discount_amount} lv.")