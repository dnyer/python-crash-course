current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

# this code makes an infinite loop
# while current_number > 0:
#	print(current_number)