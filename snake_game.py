import random
def play():
	l=["snake","water","gun"]
	print("Let\'s play the game")
	m=int(input("Enter 1 for Snake,Enter 2 for Water,Enter 3 for Gun\n"))
	del l[m-1]
	choice=random.choice(l)
	if m==1:
		if choice=="water":
			print("Congrats,You win")
			return 1
		else:
			print('Sorry,You loose')
			return 0
	elif m==2:
		if choice=='snake':
			print('Sorry,You loose')
			return 0
		else:
			print("Congrats,You win")
			return 1
	elif m==3:
		if choice=='snake':
			print("Congrats,You win")
			return 1
		else:
			print('Sorry,You loose')
			return 0
	else:
		print('You have given a invalid input')
		
		
#	i=int(input("If you want to play again enter 1, else enter 2 for exit\n"))
#	if i==1:
#		play()
#	else:
#		print('Have a good day')		
#	
#play()
print('In this game you get 10 chance')
g=1
y=0
while g<=10:
	r=play()
	y+=r
	if g<10:
		print(f"You have {10-g} more chance")
	else:
		print('You have no more chance')
	print(f'Your score is {y} out of {g}')
	g+=1
	
if y>5:
	print('Congrats,You have won the match.')
elif y==5:
	print('The match is draw')
else:
	print('You lose the match')