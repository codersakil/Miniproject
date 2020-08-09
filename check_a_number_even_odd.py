#chek a number odd or even
c=input('Please give a number:')
a=int(c)
b=a/2
import math
if b-math.floor(b)==0:
	print('it is an even number')
else:
	print('it is an odd number')