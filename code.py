flag=0
for x in range (2, 11):
	a = int (x/2) + 1
	for y in range(2, a):
		if ((x%y)==0):
			flag=flag+1
			break
	if (flag == 0):
		print (x)
	flag=0
