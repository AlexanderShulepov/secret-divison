from divider import divider
def lab():
	x=25324
	d=divider(x,4,3)
	keys=d.generate_parts()
	print (keys)
	secret=d.recovery(keys[:3])
	return(secret["value"])
print('результат:',lab())