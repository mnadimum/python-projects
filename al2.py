# make an empty list for storing aliens.

aliens = []
# make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	
# show the first 5 aliens.

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'Wine'
		alien['points'] = 100
		alien['speed'] = 'High'
	print(alien)
print("...")

for alien in aliens[:5]:
	print(alien)

# show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
print(aliens)
