import time
import random


print()
print('-' * 55)
print()


print('A wild Geodude appears!')
time.sleep(0.3)
print('...the background music changes...')
time.sleep(0.3)
print('You only have one Pokemon, Piplup!')
time.sleep(0.3)
print('I choose you Piplup!!!')
time.sleep(0.3)
print()

# set starting hp values
piplup_hp = 75

geodude_hp = 150

while piplup_hp > 0 and geodude_hp > 0:
	print('Chose your battle move:')
	time.sleep(0.3)
	print('- [1] Tackle')
	time.sleep(0.3)
	print('- [2] Bubble beam')
	time.sleep(0.3)
	print('- [3] Eat fish')
	time.sleep(0.3)
	print('- [4] Run away!')
	time.sleep(0.3)
	print()

	player_move = input('Pick a move using the corresponding number: ')
	player_move = int(player_move)

	if player_move == 1:
		geodude_hp = geodude_hp - 25
		print('Leekbird uses Tackle and deals 25 HP of damage.')

	elif player_move == 2:
		damage = random.randint(10 , 50)
		geodude_hp = geodude_hp - damage
		damage = str(damage)
		print('Piplup uses Bubble Beam and deals ' + str(damage) + ' damage to Geodude!' )

	elif player_move == 3:
		piplup_hp = piplup_hp + 40
		print('Piplup consumes fish and gains 40 HP!')


	time.sleep(0.3)
	print()


	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		piplup_hp = piplup_hp - 30
		print('Geodude uses Rock Throw and deals 30 damage.')
	elif enemy_move == 2:
		piplup_hp = piplup_hp - 15
		print('Geodude uses Double Punch and deals 15 damage to Piplup!')

	time.sleep(0.3)
	print()

	if piplup_hp < 0:
		piplup_hp = 0

	if geodude_hp < 0:
		
		geodude_hp = 0

	print('Updated HP:')
	time.sleep(0.3)
	print('Piplup HP: ' + str(piplup_hp))
	time.sleep(0.3)
	print('Geodude HP: ' + str(geodude_hp))
	time.sleep(0.3)
	print()