# points = 0
# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0)

# new_points = alien_0['points']
# points = points + new_points

# print(f"You shot down a {alien_0['color']} alien and earned {new_points} points! Your new score is {points}.")

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'medium'

# print(alien_0)

# print(f"original position: {alien_0['x_position']}")

# #move the alien to the right
# #determine how far to move the alien based on current speed

# if alien_0['speed'] == 'slow':
# 	x_increment = 1

# elif alien_0['speed'] == 'medium':
# 	x_increment = 2

# elif alien_0['speed'] == 'fast':
# 	x_increment = 3

# alien_0['x_position'] += x_increment

# print(f"new position: {alien_0['x_position']}")

# alien_size=alien_0.get('size', 'No size value assigned.')
# print(alien_size)
# alien_0['size'] = 'large'
# alien_size=alien_0.get('size', 'No size value assigned.')
# print(alien_size)

aliens = []

for idx, alien_number in enumerate(range(30)):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow', 'priority': idx}
	aliens.append(new_alien)

for idx, alien in enumerate(aliens[:5]):
	print(f"Alien#{idx}")
	print(alien)
	print("...")

for alien in aliens[:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['speed']='medium'
		alien['points']=10

for alien in aliens[:5]:
	print(alien)

print(f"Total number of aliens: {len(aliens)}")