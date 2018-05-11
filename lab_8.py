from divider import divider
from gost import gost_generate
def lab():
	x=gost_generate()
	d=divider(x,4,3)
	keys=d.generate_parts()
	print (keys	)
	secret=d.recovery(keys[:3])
	return(secret["value"])
print(lab())