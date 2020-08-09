def f2(a):
	b=2
	while b<a:
		m=a/b
		n=m-int(m)
		if n==0:
			print(a,'is a divisible number')
			break
		else:
			b+=1
	else:
		print(a,'is a non divisible number')
		
		
