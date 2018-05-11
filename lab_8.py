from divider import divider
#from gost import gost_generate
def lab():
	x=9942319#gost_generate()
	d=divider(x,5,5)
	keys=d.generate_parts()
	print (keys	)
	secret=d.recovery(keys)
	return(secret["value"])
print('результат:',lab())