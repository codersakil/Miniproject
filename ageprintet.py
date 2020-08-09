#age printer
cur_year=2020
def age(date,*year):
	if 0<date<200:
		age=cur_year-date
		c_age=cur_year-age
		cen_year=age+100
		print(f'Your current age is {c_age}')
		print(f'You will be 100 years old in {cen_year}')
		
	elif cur_year>date>1500:
		age=date
		c_age=cur_year-age
		cen_year=age+100
		print(f'Your current age is {c_age}')
		print(f'You will be 100 years old in {cen_year}')
	elif 200<=date<1500:
		print('Probably you are the oldest per son')
		
	elif date<0 or date>cur_year:
		print('You haven\'t born yet')
		
	else:
		print('You have given a wrong information')
			
	print(type(*year))
	
	try:
		g_year=year[0]
		if g_year>age:
			print(f'You will be {g_year-age} years old in {g_year}')
		elif g_year<age:
			print('You are not born till this year')
		else:
			print('You have given a wrong information')
	except Exception as e:
		print(e)
		
age(2002,2000)