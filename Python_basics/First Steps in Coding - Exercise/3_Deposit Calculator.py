deposit_amount = float(input())
deposit_period = int(input())
a_i_r = float(input())

monthly_interest = (deposit_amount * a_i_r) / 100 /12
final_amount = deposit_amount + deposit_period * monthly_interest
print(final_amount)