age=19
if age>17:
	print("you can vote!")
else:
	print("Sorry, you can't vote yet")

if age<4:
	price=0
elif age<18:
	price=20
else:
	price=30
print(f"Because you are {age} years old, your ticket costs ${price}")

