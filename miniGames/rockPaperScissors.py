import random

play = input('Would you like to play Rock, Paper, Scissors? 1 = yes, 0 = abort ')

while play == 1:

	user = raw_input("'r' for rock, 'p' for paper, 's' for scissors\n")
	computer = random.choice(['r', 'p', 's'])

	if user == computer:
		print 'tie'

	elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
		print 'You won!'

	else:
		print 'You lost :('

	print ''
	play = input('Would you like to play again? 1 = yes, 0 = abort ')

	if play == 0:
		print 'Thanks for playing, please come again.'
