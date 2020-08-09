def fabfn(n):
	a=0
	b=1
	p=0
	k=0
	while p<=n:
		print(k,end='  ')
		a=b
		b=k
		k=a+b
		p+=1
		
		

fabfn(7)