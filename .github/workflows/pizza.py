pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'cheese'],
}

print(f"You ordered a {pizza['crust']}-pizza "
	"with the following toppings: ")
for topping in pizza['toppings']:
	print(f"\t{topping}")