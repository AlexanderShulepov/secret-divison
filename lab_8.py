from divider import divider
#from gost import gost_generate
def lab():
	x=19256292#gost_generate()
	d=divider(x,11,7)
	keys=d.generate_parts()
	print (keys	)
	secret=d.recovery(keys)
	return(secret["value"])
print('результат:',lab())