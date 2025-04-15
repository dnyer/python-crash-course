toppings=['mushrooms', 'pineapple', 'sausage']

print("making pizza numero uno...")
ordered_anything = False
if 'mushrooms' in toppings:
	ordered_anything = True
	print("You ordered mushrooms")
if 'pepperoni' in toppings:
	ordered_anything = True
	print("You ordered pepperoni")
if 'sausage' in toppings:
	ordered_anything = True
	print("You ordered sausage")
if ordered_anything != True:
	print("You didn't ask for the approved toppings")

for topping in toppings:
	if topping == "pineapple":
		print(f"Sorry, we're out of {topping}")
	else:
		print(f"Added {topping} to your pizza")

toppings2=[]
print("\nmaking pizza number two...")
if toppings2:
	for topping in toppings:
		print(topping)
else:
	print("No toppings on pizza 2")


print("\nmaking pizza number 3...")
available_toppings = ['tomatoes', 'green peppers', 'sausage', 'cheese']
requested_toppings = ['green peppers', 'olives', 'cheese']

for topping in requested_toppings:
	if topping in available_toppings:
		print(f"Added {topping} to your pizza")
	else:
		print(f"Sorry, we're out of {topping}")