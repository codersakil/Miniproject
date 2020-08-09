def palin():
	a=input('Enter your word: ')
	l=len(a)-1
	p=0
	while p<len(a)/2:
		if a[p]==a[l-p]:
			p+=1
		else:
			print('The word is not palindromic')
			break
	else:
		print('The word is palindromic')
	
	
palin()
