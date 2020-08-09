
def neet(num):
	l=[]
	for aw in range(180):
		for na in range(180-aw):
			if (aw*5)+(na*4) == 720-num :
				l.append((aw,na))
				
	return l
	
if __name__=='__main__' :
	for i in range(720):
		if neet(i)== []:
			print(i)